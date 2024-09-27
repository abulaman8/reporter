from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    section = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StudentParentRelation(models.Model):
    MOM = 'mom'
    DAD = 'dad'
    GUARDIAN = 'guardian'
    RELATIONSHIP_CHOICES = [
        (MOM, 'Mom'),
        (DAD, 'Dad'),
        (GUARDIAN, 'Guardian'),
    ]
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    parent = models.ForeignKey('Parent', on_delete=models.CASCADE)
    relation_type = models.CharField(
        max_length=32, choices=RELATIONSHIP_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    roll_no = models.CharField(max_length=255, null=True, blank=True)
    class_id = models.ForeignKey(
        Class, on_delete=models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Parent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    kids = models.ManyToManyField(Student, through=StudentParentRelation)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Coach(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    kids = models.ManyToManyField(Student, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class GeneralFaculty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Report(models.Model):
    PARENT_REPORT = 'parent'
    COACH_REPORT = 'coach'
    GENERAL_FACULTY_REPORT = 'general_faculty'
    RELATIONSHIP_CHOICES = [
        (PARENT_REPORT, 'Parent'),
        (COACH_REPORT, 'Coach'),
        (GENERAL_FACULTY_REPORT, 'General Faculty'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    report_type = models.CharField(
        max_length=32, choices=RELATIONSHIP_CHOICES, default=PARENT_REPORT)
    file = models.FileField(upload_to='reports/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    session_id = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rmaxtoe = models.FloatField(null=True, blank=True)
    rmaxheel = models.FloatField(null=True, blank=True)
    lmaxtoe = models.FloatField(null=True, blank=True)
    lmaxheel = models.FloatField(null=True, blank=True)
    rmintoe = models.FloatField(null=True, blank=True)
    rminheel = models.FloatField(null=True, blank=True)
    lmintoe = models.FloatField(null=True, blank=True)
    lminheel = models.FloatField(null=True, blank=True)
    ravgtoe = models.FloatField(null=True, blank=True)
    ravgheel = models.FloatField(null=True, blank=True)
    lavgtoe = models.FloatField(null=True, blank=True)
    lavgheel = models.FloatField(null=True, blank=True)
    lflatfoot = models.FloatField(null=True, blank=True)
    rflatfoot = models.FloatField(null=True, blank=True)
    rmeancopx = models.FloatField(null=True, blank=True)
    rmeancopy = models.FloatField(null=True, blank=True)
    lmeancopx = models.FloatField(null=True, blank=True)
    lmeancopy = models.FloatField(null=True, blank=True)
    totalstepcnt = models.IntegerField(null=True, blank=True)
    lswingtimevar = models.FloatField(null=True, blank=True)
    rswingtimevar = models.FloatField(null=True, blank=True)
    lstancetimevar = models.FloatField(null=True, blank=True)
    rstancetimevar = models.FloatField(null=True, blank=True)
    avgheartbeat = models.FloatField(null=True, blank=True)
    peakheartbeat = models.FloatField(null=True, blank=True)
    minheartbeat = models.FloatField(null=True, blank=True)
    lstepcnt = models.IntegerField(null=True, blank=True)
    rstepcnt = models.IntegerField(null=True, blank=True)
    lcad = models.JSONField(null=True, blank=True)
    ltime = models.JSONField(null=True, blank=True)
    rcad = models.JSONField(null=True, blank=True)
    rtime = models.JSONField(null=True, blank=True)
    rslvar = models.FloatField(null=True, blank=True)
    lslvar = models.FloatField(null=True, blank=True)
    slasym = models.FloatField(null=True, blank=True)
    swingasym = models.FloatField(null=True, blank=True)
    stanceasym = models.FloatField(null=True, blank=True)
    rsvvar = models.FloatField(null=True, blank=True)
    lsvvar = models.FloatField(null=True, blank=True)
    svasym = models.FloatField(null=True, blank=True)
    lswingtime = models.JSONField(null=True, blank=True)
    rswingtime = models.JSONField(null=True, blank=True)
    lstancetime = models.JSONField(null=True, blank=True)
    rstancetime = models.JSONField(null=True, blank=True)
    lavgswing = models.FloatField(null=True, blank=True)
    lavgstance = models.FloatField(null=True, blank=True)
    ravgswing = models.FloatField(null=True, blank=True)
    ravgstance = models.FloatField(null=True, blank=True)
    lcadence = models.FloatField(null=True, blank=True)
    rcadence = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
