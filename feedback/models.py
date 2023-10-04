# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FeedStudent(models.Model):
    id = models.IntegerField(primary_key=True)
    reg = models.CharField(max_length=264)
    deptid = models.IntegerField()
    gender = models.CharField(max_length=264)
    name = models.CharField(max_length=264)
    nos = models.IntegerField()
    quota = models.CharField(max_length=264)
    s1 = models.CharField(max_length=264)
    s2 = models.CharField(max_length=264)
    secid = models.CharField(max_length=264)
    set1 = models.CharField(max_length=264)
    yearid = models.CharField(max_length=264)

    class Meta:
        managed = False
        db_table = 'feed_student'


class Mark(models.Model):
    roll_no = models.CharField(max_length=20, blank=True, null=True)
    sem = models.CharField(max_length=10, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    internal1 = models.IntegerField(blank=True, null=True)
    internal2 = models.IntegerField(blank=True, null=True)
    internal3 = models.IntegerField(blank=True, null=True)
    assessment1 = models.IntegerField(blank=True, null=True)
    assessment2 = models.IntegerField(blank=True, null=True)
    assessment3 = models.IntegerField(blank=True, null=True)
    unittest1 = models.IntegerField(db_column='unitTest1', blank=True, null=True)  # Field name made lowercase.
    unittest2 = models.IntegerField(db_column='unitTest2', blank=True, null=True)  # Field name made lowercase.
    unittest3 = models.IntegerField(db_column='unitTest3', blank=True, null=True)  # Field name made lowercase.
    staff_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mark'


class StaffFiles(models.Model):
    ids = models.AutoField(primary_key=True)
    staff_id = models.CharField(max_length=30, blank=True, null=True)
    file_name = models.TextField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    journal = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    host = models.TextField(blank=True, null=True)
    tot_stu = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)
    dept = models.CharField(max_length=20, blank=True, null=True)
    submission = models.CharField(max_length=200, blank=True, null=True)
    amount = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_files'


class StaffSignup(models.Model):
    staff_id = models.CharField(primary_key=True, max_length=30)
    staff_name = models.CharField(max_length=100, blank=True, null=True)
    staff_email = models.TextField(blank=True, null=True)
    staff_password = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_signup'


class StaffUploads(models.Model):
    ids = models.AutoField(primary_key=True)
    event_type = models.TextField(blank=True, null=True)
    event_name = models.TextField(blank=True, null=True)
    event_title = models.TextField(blank=True, null=True)
    event_host = models.TextField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    files = models.TextField(blank=True, null=True)
    file_name = models.TextField(blank=True, null=True)
    staff_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_uploads'


class Stu(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stu'


class Stud(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stud'


class StudentFiles(models.Model):
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    event_type = models.TextField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    event_org = models.TextField(blank=True, null=True)
    ac_year = models.TextField(blank=True, null=True)
    event_title = models.TextField(blank=True, null=True)
    roll_no = models.CharField(max_length=40, blank=True, null=True)
    ids = models.AutoField(primary_key=True)
    dept = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    batch = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_files'


class StudentSignup(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    roll_no = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=15, blank=True, null=True)
    mobile_no = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    tenth_mark = models.IntegerField(blank=True, null=True)
    twelth_mark = models.IntegerField(blank=True, null=True)
    twelth_cutoff = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    school = models.CharField(max_length=255, blank=True, null=True)
    cgpa = models.IntegerField(blank=True, null=True)
    dept = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    batch = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_signup'


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
