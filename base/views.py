from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Admin, Student, Parent, GeneralFaculty, Coach
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from allauth.account.views import LoginView
from allauth.account.forms import LoginForm
from django.shortcuts import redirect, render
from django.contrib import messages
from allauth.account.views import SignupView, LoginView
from .forms import CustomSignupForm
import pandas as pd
from utils.heart_rate import plot_heart_rate
from utils.cadence_gauge import cad_plot
from utils.cad_bpm_plot import cad_bpm_plot
from utils.cad_bpm_rank import cad_bpm_rank
from utils.foot_pressure import pressure_plot
from utils.cop import cop_plot
from utils.assym import assym_plot
from utils.stride_radar import stride_radar_plot
import requests
import json


class CustomSignupView(SignupView):
    template_name = "account/signup.html"
    form_class = CustomSignupForm

    def form_valid(self, form):

        user = form.save(self.request)
        messages.success(self.request, "Account created successfully!")
        return redirect("account_login")

    def form_invalid(self, form):

        for error in form.errors.values():
            messages.error(self.request, error)
        return self.render_to_response(self.get_context_data(form=form))


def index(request):
    return render(request, "base/home.html")


@login_required
def base(request):
    user = request.user
    if Admin.objects.filter(user=user).exists():
        return redirect("admin_dashboard")
    elif Student.objects.filter(user=user).exists():
        return redirect("student_dashboard")
    elif Parent.objects.filter(user=user).exists():
        return redirect("parent_dashboard")
    elif GeneralFaculty.objects.filter(user=user).exists():
        return redirect("faculty_dashboard")
    elif Coach.objects.filter(user=user).exists():
        return redirect("coach_dashboard")
    else:
        logout(request)
        messages.error(
            request, "No associated role found for this user.")
        return redirect("account_login")


def view_report(request):

    ssnid = request.POST.get('sessionid')
    student_id = request.POST.get('studentid')
    data = {
        "ssnid": int(ssnid),
        "studentid": str(student_id)
    }
    try:

        req = requests.get(
            'http://10.21.170.133:8000/api/reportdata/',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(data)
        )
        student_data_req = requests.get(
            "http://10.21.170.133:8000/api/schldetail/",
            headers={'Content-Type': 'application/json'},
            # data=json.dumps({"sid": "20002"})
            data=json.dumps({"sid": str(student_id)})
        )
        print(req.status_code)
        res = req.json()
        student_data = student_data_req.json()
        student_data_status = student_data.get("status")
    except Exception as e:
        print(e)
        messages.error(request, f"{e}")
        return render(request, "base/home.html")
    if len(res) == 0:
        messages.error(
            request, f"No report found for student id {student_id} and session id {ssnid}.")
        return render(request, "base/home.html")
    heart_beat_metrics = res[7]["heartbeat metrics"]
    cadence_metrics = res[6]["cadence metrics"]
    stride_metrics = res[8]["stride metrics"]
    stance_metrics = res[5]["stance metrics"]
    swing_metrics = res[4]["swing metrics"]
    cop_metrics = res[2]["cop metrics"]
    pressure_metrics = res[0]["pressure metrics"]

    data = {
        "name": student_data["name"] if student_data_status == "success" else "",
        "age": student_data["age"] if student_data_status == "success" else "",
        # "gender": student_data["gender"] if student_data_status == "success" else "",
        "height": student_data["height"] if student_data_status == "success" else "",
        "body_mass": student_data["weight"] if student_data_status == "success" else "",
        "heart_rate": heart_beat_metrics[0]["avgheartbeat"],
        "cadence": cadence_metrics[0]["rmeancadence"],
        "right_toe_pressure": round(pressure_metrics[0]["ravgtoe"], 2),
        "left_toe_pressure": round(pressure_metrics[0]["lavgtoe"], 2),
        "right_heel_pressure": round(pressure_metrics[0]["ravgheel"], 2),
        "left_heel_pressure": round(pressure_metrics[0]["lavgheel"], 2),
        "walking_avg_bpm": heart_beat_metrics[0]["avgheartbeat"],
        "walking_min_bpm": heart_beat_metrics[0]["minheartbeat"],
        "walking_max_bpm": heart_beat_metrics[0]["peakheartbeat"],
        "running_avg_bpm": heart_beat_metrics[0]["avgheartbeat"],
        "running_min_bpm": heart_beat_metrics[0]["minheartbeat"],
        "running_max_bpm": heart_beat_metrics[0]["peakheartbeat"],
        "jumping_avg_bpm": heart_beat_metrics[0]["avgheartbeat"],
        "jumping_min_bpm": heart_beat_metrics[0]["minheartbeat"],
        "jumping_max_bpm": heart_beat_metrics[0]["peakheartbeat"],
        "right_cop": round((((cop_metrics[0]["rmeancopx"] ** 2) + (cop_metrics[0]["rmeancopy"] ** 2)) ** 0.5)/10, 2),
        "left_cop": round((((cop_metrics[0]["lmeancopx"] ** 2) + (cop_metrics[0]["lmeancopy"] ** 2)) ** 0.5)/10, 2),
        "stride_length": round(stride_metrics[0]["lmnstridelen"], 2),
        "stride_length_variability": round(stride_metrics[0]["rstridelenvar"], 2),
        "stride_velocity": round(stride_metrics[0]["lmnstrideavelo"], 2),
        "stride_velocity_variability": round(stride_metrics[0]["lstridevelovar"], 2),
        "swing_time": round(swing_metrics[0]["lavgswing"], 2),
        "stance_time": round(stance_metrics[0]["lavgstance"], 2),
        "swing_time_variability": round(swing_metrics[0]["lswingtimevar"], 2),
        "stance_time_variability": round(stance_metrics[0]["lstancetimevar"], 2),
        "stride_length_assymetry": round(stride_metrics[0]["stridelenasym"], 2),
        "swing_time_assymetry": round(swing_metrics[0]["swingasym"], 2),
        "stance_time_assymetry": round(stance_metrics[0]["stanceasym"], 2),
        "heart_rate_img": plot_heart_rate(
            [heart_beat_metrics[0]["minheartbeat"], heart_beat_metrics[0]["minheartbeat"],
             heart_beat_metrics[0]["minheartbeat"]],
            [heart_beat_metrics[0]["avgheartbeat"], heart_beat_metrics[0]["avgheartbeat"],
             heart_beat_metrics[0]["avgheartbeat"]],
            [heart_beat_metrics[0]["peakheartbeat"], heart_beat_metrics[0]["peakheartbeat"],
             heart_beat_metrics[0]["peakheartbeat"]],
        ),
        "cadence_img": cad_plot(round(cadence_metrics[0]["rmeancadence"], 2) if cadence_metrics[0]["rmeancadence"] else 114),
        "cadence_vs_heart_rate_img": cad_bpm_plot(
            round(cadence_metrics[0]["rmeancadence"],
                  2) if cadence_metrics[0]["rmeancadence"] else 114,
            heart_beat_metrics[0]["avgheartbeat"] if heart_beat_metrics[0]["avgheartbeat"] else 94),
        "pressure_img": pressure_plot(
            round(pressure_metrics[0]["lavgtoe"], 2),
            round(pressure_metrics[0]["lavgheel"], 2),
            round(pressure_metrics[0]["ravgtoe"], 2),
            round(pressure_metrics[0]["ravgheel"], 2),
        ),
        "cop_img": cop_plot([
            round((((cop_metrics[0]["lmeancopx"] ** 2) +
                    (cop_metrics[0]["lmeancopy"] ** 2)) ** 0.5)/10, 2),
            round((((cop_metrics[0]["rmeancopx"] ** 2) +
                    (cop_metrics[0]["rmeancopy"] ** 2)) ** 0.5)/10, 2)
        ]),
        "assymetry_img": assym_plot([
            round(stride_metrics[0]["stridelenasym"],
                  2) if stride_metrics[0]["stridelenasym"] else 5,
            round(stride_metrics[0]["strideveloasym"],
                  2) if stride_metrics[0]["strideveloasym"] else 5,
            round(swing_metrics[0]["swingasym"],
                  2) if swing_metrics[0]["swingasym"] else 8,
            round(stance_metrics[0]["stanceasym"],
                  2) if stance_metrics[0]["stanceasym"] else 4,
        ]),
        "stride_radar_img": stride_radar_plot([
            round(stride_metrics[0]["lmnstridelen"], 2),
            round(stride_metrics[0]["lmnstrideavelo"], 2),
            round(swing_metrics[0]["lavgswing"], 2),
            round(stance_metrics[0]["lavgstance"], 2),
        ]
        )



    }
    return render(request, "base/index.html", data)