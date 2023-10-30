from django.contrib.auth.models import AbstractUser
from django.db import models


class UserInfo(AbstractUser):
    nid = models.AutoField(primary_key=True)
    tel = models.CharField(verbose_name='phone number', max_length=12, null=True, blank=True)
    addr = models.CharField(max_length=8, verbose_name='address', null=True, blank=True)
    name = models.CharField(max_length=8, verbose_name='name', null=True, blank=True)
    sex = models.CharField(max_length=2, verbose_name='sex', null=True, blank=True)
    student_id = models.CharField(max_length=128, verbose_name='student id', null=True, blank=True)
    age = models.IntegerField(verbose_name='age', null=True, blank=True)
    id_card = models.CharField(verbose_name='identity id', max_length=64, null=True, blank=True)
    role = models.CharField(verbose_name='user role', max_length=16, default='student')

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name_plural = 'user inf'


class House(models.Model):
    nid = models.AutoField(primary_key=True)
    housing_no = models.CharField(max_length=256, verbose_name='room number', null=True)
    building_no = models.CharField(max_length=256, verbose_name='building number', null=True, blank=True)
    construction_area = models.CharField(max_length=256, verbose_name='building area', null=True, blank=True)
    using_area = models.CharField(max_length=256, verbose_name='used area', null=True, blank=True)
    type = models.CharField(max_length=256, verbose_name='building type', null=True, blank=True)
    addr = models.CharField(max_length=256, verbose_name='address', null=True, blank=True)
    location = models.CharField(max_length=256, verbose_name='coordinate', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='create time', auto_now_add=True, null=True)
    user_name = models.CharField(max_length=8, verbose_name='owner', null=True, blank=True)

    def __str__(self):
        return self.housing_no

    class Meta:
        verbose_name_plural = 'house inf'


class CrimeRate(models.Model):
    nid = models.AutoField(primary_key=True)
    X = models.CharField(max_length=256, null=True, blank=True)
    Y = models.CharField(max_length=256, null=True, blank=True)
    FID = models.CharField(max_length=256, null=True, blank=True)
    Year = models.CharField(max_length=256, null=True, blank=True)
    ReportDate = models.CharField(max_length=256, null=True, blank=True)
    ReportTime = models.CharField(max_length=256, null=True, blank=True)
    OccurDate = models.CharField(max_length=256, null=True, blank=True)
    Occur_Time = models.CharField(max_length=256, null=True, blank=True)
    Weekday = models.CharField(max_length=256, null=True, blank=True)
    OffSummary = models.CharField(max_length=256, null=True, blank=True)
    PrimViolat = models.CharField(max_length=256, null=True, blank=True)
    Neighbourh = models.CharField(max_length=256, null=True, blank=True)
    Sector = models.CharField(max_length=256, null=True, blank=True)
    Division = models.CharField(max_length=256, null=True, blank=True)
    CensusTra = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return str(self.X)

    class Meta:
        verbose_name_plural = 'crime rate'


