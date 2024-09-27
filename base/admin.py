from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from .models import Coach, School, Student, Session, StudentParentRelation, Parent, Report, GeneralFaculty, Class


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(School)
class SchoolAdmin(ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(Student)
class StudentAdmin(ModelAdmin):
    list_display = ('name', 'roll_no')
    search_fields = ('name', 'roll_no', 'class_id__name')


@admin.register(Report)
class ReportAdmin(ModelAdmin):
    list_display = ('name', 'student', 'report_type')
    search_fields = ('name', 'student__name', 'report_type')


@admin.register(StudentParentRelation)
class StudentParentRelationAdmin(ModelAdmin):
    list_display = ('student', 'parent')
    search_fields = ('student__name', 'parent__name')


@admin.register(Parent)
class ParentAdmin(ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')


@admin.register(GeneralFaculty)
class GeneralFacultyAdmin(ModelAdmin):
    list_display = ('name', 'school')
    search_fields = ('name', 'school__name')


@admin.register(Class)
class ClassAdmin(ModelAdmin):
    list_display = ('name', 'section', 'school')
    search_fields = ('name', 'section', 'school__name')


@admin.register(Coach)
class CoachAdmin(ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__username')


@admin.register(Session)
class SessionAdmin(ModelAdmin):
    list_display = ('session_id', 'student',)
    search_fields = ('session_id', 'student__name')
