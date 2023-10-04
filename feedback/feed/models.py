# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    reg = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    quota = models.CharField(max_length=255)
    deptid = models.IntegerField()
    yearid = models.CharField(max_length=5)
    secid = models.CharField(max_length=255)
    set1 = models.CharField(max_length=255)
    nos = models.IntegerField()
    s1 = models.CharField(max_length=10)
    s2 = models.CharField(max_length=10)
    s3 = models.CharField(max_length=10)
    s4 = models.CharField(max_length=10)
    s5 = models.CharField(max_length=10)
    s6 = models.CharField(max_length=10)
    s7 = models.CharField(max_length=10)
    password = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'students'
