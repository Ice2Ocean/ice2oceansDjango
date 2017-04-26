# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gis_models


# Notes from AArendt: Delete these tables from ice2ocean
# arendtregions
# burgessregions
# ergi
# ergibins
# icesat
# lamb
# mascon_fit
# mascon_solution
# prism
# snowradar_old
# sweingest_lines
# sweingest_metadata



# class Arendtregions(models.Model):
#     arendtid = models.IntegerField(primary_key=True)
#     paperid = models.IntegerField(blank=True, null=True)
#     region = models.CharField(max_length=500, blank=True, null=True)
#     albersgeom = gis_models.GeometryField(blank=True, null=True, srid=3338)
#
#     class Meta:
#         managed = True
#         db_table = 'arendtregions'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Boundaries(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'boundaries'


# class Burgessregions(models.Model):
#     burgessid = models.IntegerField(primary_key=True)
#     region = models.CharField(max_length=500, blank=True, null=True)
#     albersgeom = gis_models.GeometryField(blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'burgessregions'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class DrawWire(models.Model):
    station_name = models.TextField(blank=True, null=True)
    extension = models.FloatField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    gid = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'draw_wire'


# class Ergi(models.Model):
#     glimsid = models.CharField(max_length=500, blank=True, null=True)
#     max = models.IntegerField(blank=True, null=True)
#     min = models.IntegerField(blank=True, null=True)
#     area = models.FloatField(blank=True, null=True)
#     albersgeom = gis_models.GeometryField(blank=True, null=True)
#     name = models.CharField(max_length=50, blank=True, null=True)
#     gltype = models.CharField(max_length=500, blank=True, null=True)
#     ergiid = models.AutoField(primary_key=True)
#
#     class Meta:
#         managed = True
#         db_table = 'ergi'


# class Ergibins(models.Model):
#     ergibinsid = models.AutoField(primary_key=True)
#     glimsid = models.CharField(max_length=254, blank=True, null=True)
#     bins = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
#     area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
#     albersgeom = gis_models.GeometryField(blank=True, null=True)
#     normbins = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'ergibins'


class Glacierwidebal(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    season = models.CharField(max_length=254, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'glacierwidebal'


# class Icesat(models.Model):
#     t_mean = models.IntegerField(blank=True, null=True)
#     t_min = models.IntegerField(blank=True, null=True)
#     t_max = models.IntegerField(blank=True, null=True)
#     h_ell = models.FloatField(blank=True, null=True)
#     geoid = models.FloatField(blank=True, null=True)
#     h_orto = models.FloatField(blank=True, null=True)
#     h_dem = models.FloatField(blank=True, null=True)
#     gain = models.FloatField(blank=True, null=True)
#     reftracknr = models.IntegerField(blank=True, null=True)
#     stripnr = models.FloatField(blank=True, null=True)
#     planenr = models.IntegerField(blank=True, null=True)
#     eslope = models.FloatField(blank=True, null=True)
#     nslope = models.FloatField(blank=True, null=True)
#     slope = models.FloatField(blank=True, null=True)
#     aspect = models.FloatField(blank=True, null=True)
#     dir = models.FloatField(blank=True, null=True)
#     rms = models.FloatField(blank=True, null=True)
#     dhdt = models.FloatField(blank=True, null=True)
#     nrofprofs = models.SmallIntegerField(blank=True, null=True)
#     nrofpoints = models.SmallIntegerField(blank=True, null=True)
#     region = models.SmallIntegerField(blank=True, null=True)
#     longitude = models.FloatField(blank=True, null=True)
#     latitude = models.FloatField(blank=True, null=True)
#     load_tide = models.FloatField(blank=True, null=True)
#     ocean_tide = models.FloatField(blank=True, null=True)
#     time_mean = models.DateField(blank=True, null=True)
#     time_min = models.DateField(blank=True, null=True)
#     time_max = models.DateField(blank=True, null=True)
#     geom = gis_models.GeometryField(blank=True, null=True)
#     gid = models.AutoField(primary_key=True)
#
#     class Meta:
#         managed = True
#         db_table = 'icesat'


# class Lamb(models.Model):
#     lambid = models.AutoField(primary_key=True)
#     glimsid = models.CharField(max_length=14, blank=True, null=True)
#     date1 = models.DateField(blank=True, null=True)
#     date2 = models.DateField(blank=True, null=True)
#     interval = models.SmallIntegerField(blank=True, null=True)
#     volmodel = models.FloatField(blank=True, null=True)
#     vol25diff = models.FloatField(blank=True, null=True)
#     vol75diff = models.FloatField(blank=True, null=True)
#     balmodel = models.FloatField(blank=True, null=True)
#     bal25diff = models.FloatField(blank=True, null=True)
#     bal75diff = models.FloatField(blank=True, null=True)
#     e = models.TextField(blank=True, null=True)  # This field type is a guess.
#     dz = models.TextField(blank=True, null=True)  # This field type is a guess.
#     dz25 = models.TextField(blank=True, null=True)  # This field type is a guess.
#     dz75 = models.TextField(blank=True, null=True)  # This field type is a guess.
#     aad = models.TextField(blank=True, null=True)  # This field type is a guess.
#     masschange = models.TextField(blank=True, null=True)  # This field type is a guess.
#     massbal = models.TextField(blank=True, null=True)  # This field type is a guess.
#     numdata = models.TextField(blank=True, null=True)  # This field type is a guess.
#
#     class Meta:
#         managed = True
#         db_table = 'lamb'


class LambEarly(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    balance_error = models.FloatField(db_column='Balance_error', blank=True, null=True)  # Field name made lowercase.
    balance_areaavg = models.FloatField(db_column='Balance_areaAvg', blank=True, null=True)  # Field name made lowercase.
    balance_areaavg_error = models.FloatField(db_column='Balance_areaAvg_error', blank=True, null=True)  # Field name made lowercase.
    start_date = models.FloatField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    source = models.CharField(max_length=254, blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lamb_early'


class Mapdate(models.Model):
    gid = models.AutoField(primary_key=True)
    rgiid = models.CharField(max_length=14, blank=True, null=True)
    glimsid = models.CharField(max_length=14, blank=True, null=True)
    rgiflag = models.CharField(max_length=14, blank=True, null=True)
    bgndate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    cenlon = models.FloatField(blank=True, null=True)
    cenlat = models.FloatField(blank=True, null=True)
    o1region = models.SmallIntegerField(blank=True, null=True)
    o2region = models.SmallIntegerField(blank=True, null=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    glactype = models.CharField(max_length=4, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    park = models.CharField(max_length=4, blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    avg = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mapdate'


# class MasconFit(models.Model):
#     did = models.AutoField(primary_key=True)
#     mascon = models.IntegerField(blank=True, null=True)
#     area_deg = models.FloatField(blank=True, null=True)
#     area_km2 = models.FloatField(blank=True, null=True)
#     geom = gis_models.GeometryField(blank=True, null=True)
#     version = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'mascon_fit'


# class MasconSolution(models.Model):
#     sid = models.AutoField(primary_key=True)
#     date = models.DateTimeField(blank=True, null=True)
#     mascon = models.IntegerField(blank=True, null=True)
#     values_filter1d = models.FloatField(blank=True, null=True)
#     version = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'mascon_solution'


class Modern(models.Model):
    modernid = models.AutoField(primary_key=True)
    rgiid = models.CharField(max_length=14, blank=True, null=True)
    glimsid = models.CharField(max_length=14, blank=True, null=True)
    rgiflag = models.CharField(max_length=14, blank=True, null=True)
    bgndate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    cenlon = models.FloatField(blank=True, null=True)
    cenlat = models.FloatField(blank=True, null=True)
    o1region = models.SmallIntegerField(blank=True, null=True)
    o2region = models.SmallIntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    glactype = models.CharField(max_length=4, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modern'


class ModernAreaLength(models.Model):
    modernarealengthid = models.AutoField(primary_key=True)
    modernid = models.ForeignKey(Modern, on_delete=models.CASCADE, db_column='modernid',
                                 default=27546)
    glimsid = models.CharField(max_length=254, blank=True, null=True)
    len_min = models.IntegerField(blank=True, null=True)
    len_5 = models.IntegerField(blank=True, null=True)
    len_10 = models.IntegerField(blank=True, null=True)
    len_15 = models.IntegerField(blank=True, null=True)
    len_20 = models.IntegerField(blank=True, null=True)
    len_25 = models.IntegerField(blank=True, null=True)
    len_30 = models.IntegerField(blank=True, null=True)
    len_35 = models.IntegerField(blank=True, null=True)
    len_40 = models.IntegerField(blank=True, null=True)
    len_45 = models.IntegerField(blank=True, null=True)
    len_med = models.IntegerField(blank=True, null=True)
    len_55 = models.IntegerField(blank=True, null=True)
    len_60 = models.IntegerField(blank=True, null=True)
    len_65 = models.IntegerField(blank=True, null=True)
    len_70 = models.IntegerField(blank=True, null=True)
    len_75 = models.IntegerField(blank=True, null=True)
    len_80 = models.IntegerField(blank=True, null=True)
    len_85 = models.IntegerField(blank=True, null=True)
    len_90 = models.IntegerField(blank=True, null=True)
    len_95 = models.IntegerField(blank=True, null=True)
    len_max = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modern_area_length'


class ModernDebris(models.Model):
    gid = models.AutoField(primary_key=True)
    field1 = models.IntegerField(blank=True, null=True)
    glimsid = models.CharField(max_length=254, blank=True, null=True)
    deblen_5 = models.IntegerField(blank=True, null=True)
    deblen_10 = models.IntegerField(blank=True, null=True)
    deblen_15 = models.IntegerField(blank=True, null=True)
    deblen_20 = models.IntegerField(blank=True, null=True)
    deblen_25 = models.IntegerField(blank=True, null=True)
    deblen_30 = models.IntegerField(blank=True, null=True)
    deblen_35 = models.IntegerField(blank=True, null=True)
    deblen_40 = models.IntegerField(blank=True, null=True)
    deblen_45 = models.IntegerField(blank=True, null=True)
    deblen_50 = models.IntegerField(blank=True, null=True)
    deblen_55 = models.IntegerField(blank=True, null=True)
    deblen_60 = models.IntegerField(blank=True, null=True)
    deblen_65 = models.IntegerField(blank=True, null=True)
    deblen_70 = models.IntegerField(blank=True, null=True)
    deblen_75 = models.IntegerField(blank=True, null=True)
    deblen_80 = models.IntegerField(blank=True, null=True)
    deblen_85 = models.IntegerField(blank=True, null=True)
    deblen_90 = models.IntegerField(blank=True, null=True)
    deblen_95 = models.IntegerField(blank=True, null=True)
    deblen_100 = models.IntegerField(blank=True, null=True)
    debele_5 = models.IntegerField(blank=True, null=True)
    debele_10 = models.IntegerField(blank=True, null=True)
    debele_15 = models.IntegerField(blank=True, null=True)
    debele_20 = models.IntegerField(blank=True, null=True)
    debele_25 = models.IntegerField(blank=True, null=True)
    debele_30 = models.IntegerField(blank=True, null=True)
    debele_35 = models.IntegerField(blank=True, null=True)
    debele_40 = models.IntegerField(blank=True, null=True)
    debele_45 = models.IntegerField(blank=True, null=True)
    debele_50 = models.IntegerField(blank=True, null=True)
    debele_55 = models.IntegerField(blank=True, null=True)
    debele_60 = models.IntegerField(blank=True, null=True)
    debele_65 = models.IntegerField(blank=True, null=True)
    debele_70 = models.IntegerField(blank=True, null=True)
    debele_75 = models.IntegerField(blank=True, null=True)
    debele_80 = models.IntegerField(blank=True, null=True)
    debele_85 = models.IntegerField(blank=True, null=True)
    debele_90 = models.IntegerField(blank=True, null=True)
    debele_95 = models.IntegerField(blank=True, null=True)
    debele_100 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modern_debris'


class ModernSlopes(models.Model):
    gid = models.AutoField(primary_key=True)
    glimsid = models.CharField(max_length=254, blank=True, null=True)
    slope_5 = models.SmallIntegerField(blank=True, null=True)
    slope_10 = models.SmallIntegerField(blank=True, null=True)
    slope_15 = models.SmallIntegerField(blank=True, null=True)
    slope_20 = models.SmallIntegerField(blank=True, null=True)
    slope_25 = models.SmallIntegerField(blank=True, null=True)
    slope_30 = models.SmallIntegerField(blank=True, null=True)
    slope_35 = models.SmallIntegerField(blank=True, null=True)
    slope_40 = models.SmallIntegerField(blank=True, null=True)
    slope_45 = models.SmallIntegerField(blank=True, null=True)
    slope_50 = models.SmallIntegerField(blank=True, null=True)
    slope_55 = models.SmallIntegerField(blank=True, null=True)
    slope_60 = models.SmallIntegerField(blank=True, null=True)
    slope_65 = models.SmallIntegerField(blank=True, null=True)
    slope_70 = models.SmallIntegerField(blank=True, null=True)
    slope_75 = models.SmallIntegerField(blank=True, null=True)
    slope_80 = models.SmallIntegerField(blank=True, null=True)
    slope_85 = models.SmallIntegerField(blank=True, null=True)
    slope_90 = models.SmallIntegerField(blank=True, null=True)
    slope_95 = models.SmallIntegerField(blank=True, null=True)
    slope_100 = models.SmallIntegerField(blank=True, null=True)
    eslope_5 = models.SmallIntegerField(blank=True, null=True)
    eslope_10 = models.SmallIntegerField(blank=True, null=True)
    eslope_15 = models.SmallIntegerField(blank=True, null=True)
    eslope_20 = models.SmallIntegerField(blank=True, null=True)
    eslope_25 = models.SmallIntegerField(blank=True, null=True)
    eslope_30 = models.SmallIntegerField(blank=True, null=True)
    eslope_35 = models.SmallIntegerField(blank=True, null=True)
    eslope_40 = models.SmallIntegerField(blank=True, null=True)
    eslope_45 = models.SmallIntegerField(blank=True, null=True)
    eslope_50 = models.SmallIntegerField(blank=True, null=True)
    eslope_55 = models.SmallIntegerField(blank=True, null=True)
    eslope_60 = models.SmallIntegerField(blank=True, null=True)
    eslope_65 = models.SmallIntegerField(blank=True, null=True)
    eslope_70 = models.SmallIntegerField(blank=True, null=True)
    eslope_75 = models.SmallIntegerField(blank=True, null=True)
    eslope_80 = models.SmallIntegerField(blank=True, null=True)
    eslope_85 = models.SmallIntegerField(blank=True, null=True)
    eslope_90 = models.SmallIntegerField(blank=True, null=True)
    eslope_95 = models.SmallIntegerField(blank=True, null=True)
    eslope_100 = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modern_slopes'


class Modernadditional(models.Model):
    gid = models.AutoField(primary_key=True)
    glimsid = models.CharField(max_length=14, blank=True, null=True)
    perimeter = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    compactn = models.FloatField(blank=True, null=True)
    slope = models.SmallIntegerField(blank=True, null=True)
    slope_ton = models.SmallIntegerField(blank=True, null=True)
    slope_med = models.SmallIntegerField(blank=True, null=True)
    slope_b50 = models.SmallIntegerField(blank=True, null=True)
    slope_a50 = models.SmallIntegerField(blank=True, null=True)
    aspect = models.SmallIntegerField(blank=True, null=True)
    aspect_tx = models.CharField(max_length=50, blank=True, null=True)
    aspect_b50 = models.SmallIntegerField(blank=True, null=True)
    aspect_a50 = models.SmallIntegerField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    angle = models.SmallIntegerField(blank=True, null=True)
    dist_point = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debris = models.SmallIntegerField(blank=True, null=True)
    debris_tx = models.CharField(max_length=50, blank=True, null=True)
    elev_mean = models.IntegerField(blank=True, null=True)
    elev_min = models.IntegerField(blank=True, null=True)
    sk = models.FloatField(blank=True, null=True)
    elev_5 = models.IntegerField(blank=True, null=True)
    elev_10 = models.IntegerField(blank=True, null=True)
    elev_15 = models.IntegerField(blank=True, null=True)
    elev_20 = models.IntegerField(blank=True, null=True)
    elev_25 = models.IntegerField(blank=True, null=True)
    elev_30 = models.IntegerField(blank=True, null=True)
    elev_35 = models.IntegerField(blank=True, null=True)
    elev_40 = models.IntegerField(blank=True, null=True)
    elev_45 = models.IntegerField(blank=True, null=True)
    elev_med = models.IntegerField(blank=True, null=True)
    elev_55 = models.IntegerField(blank=True, null=True)
    elev_60 = models.IntegerField(blank=True, null=True)
    elev_65 = models.IntegerField(blank=True, null=True)
    elev_70 = models.IntegerField(blank=True, null=True)
    elev_75 = models.IntegerField(blank=True, null=True)
    elev_80 = models.IntegerField(blank=True, null=True)
    elev_85 = models.IntegerField(blank=True, null=True)
    elev_90 = models.IntegerField(blank=True, null=True)
    elev_95 = models.IntegerField(blank=True, null=True)
    elev_max = models.IntegerField(blank=True, null=True)
    p_wi = models.IntegerField(blank=True, null=True)
    p_su = models.IntegerField(blank=True, null=True)
    t_wi = models.IntegerField(blank=True, null=True)
    t_su = models.IntegerField(blank=True, null=True)
    p_wi_med = models.IntegerField(blank=True, null=True)
    p_su_med = models.IntegerField(blank=True, null=True)
    t_wi_med = models.IntegerField(blank=True, null=True)
    t_su_med = models.IntegerField(blank=True, null=True)
    lenland = models.IntegerField(blank=True, null=True)
    lendiv = models.IntegerField(blank=True, null=True)
    lentdw = models.IntegerField(blank=True, null=True)
    lenlake = models.IntegerField(blank=True, null=True)
    watersh = models.FloatField(blank=True, null=True)
    lenlanddeb = models.IntegerField(blank=True, null=True)
    errorcat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modernadditional'


class Modernbinned(models.Model):
    gid = models.AutoField(primary_key=True)
    glimsid = models.CharField(max_length=254, blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modernbinned'


class Modernbinned10M(models.Model):
    gid = models.AutoField(primary_key=True)
    glimsid = models.CharField(max_length=254, blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modernbinned_10m'


class Moderncenterlines(models.Model):
    gid = models.AutoField(primary_key=True)
    glimsid = models.CharField(max_length=254, blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    main = models.SmallIntegerField(blank=True, null=True)
    lenorder = models.IntegerField(blank=True, null=True)
    ratio = models.FloatField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'moderncenterlines'


class ModerncenterlinesAspectsSlopes(models.Model):
    gid = models.AutoField(primary_key=True)
    glimsid = models.CharField(max_length=254, blank=True, null=True)
    length = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main = models.SmallIntegerField(blank=True, null=True)
    lenorder = models.IntegerField(blank=True, null=True)
    slope = models.FloatField(blank=True, null=True)
    slope_tx = models.CharField(max_length=50, blank=True, null=True)
    aspect = models.SmallIntegerField(blank=True, null=True)
    aspect_tx = models.CharField(max_length=50, blank=True, null=True)
    slope_5 = models.FloatField(blank=True, null=True)
    slope_15 = models.FloatField(blank=True, null=True)
    slope_25 = models.FloatField(blank=True, null=True)
    slope_35 = models.FloatField(blank=True, null=True)
    slope_45 = models.FloatField(blank=True, null=True)
    slope_55 = models.FloatField(blank=True, null=True)
    slope_65 = models.FloatField(blank=True, null=True)
    slope_75 = models.FloatField(blank=True, null=True)
    slope_85 = models.FloatField(blank=True, null=True)
    slope_95 = models.FloatField(blank=True, null=True)
    aspect_5 = models.SmallIntegerField(blank=True, null=True)
    aspect_15 = models.SmallIntegerField(blank=True, null=True)
    aspect_25 = models.SmallIntegerField(blank=True, null=True)
    aspect_35 = models.SmallIntegerField(blank=True, null=True)
    aspect_45 = models.SmallIntegerField(blank=True, null=True)
    aspect_55 = models.SmallIntegerField(blank=True, null=True)
    aspect_65 = models.SmallIntegerField(blank=True, null=True)
    aspect_75 = models.SmallIntegerField(blank=True, null=True)
    aspect_85 = models.SmallIntegerField(blank=True, null=True)
    aspect_95 = models.SmallIntegerField(blank=True, null=True)
    start_elev = models.IntegerField(blank=True, null=True)
    end_elev = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'moderncenterlines_aspects_slopes'


class ModerncenterlinesFlipped(models.Model):
    gid = models.AutoField(primary_key=True)
    glimsid = models.CharField(max_length=254, blank=True, null=True)
    length_br = models.FloatField(blank=True, null=True)
    main = models.SmallIntegerField(blank=True, null=True)
    order_le = models.IntegerField(blank=True, null=True)
    branch_tot = models.IntegerField(blank=True, null=True)
    multiple = models.SmallIntegerField(blank=True, null=True)
    startlen = models.IntegerField(blank=True, null=True)
    endlen = models.IntegerField(blank=True, null=True)
    ratio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'moderncenterlines_flipped'


class ModerncenterlinesHypsometry(models.Model):
    gid = models.AutoField(primary_key=True)
    glimsid = models.CharField(max_length=14, blank=True, null=True)
    elev_mean = models.IntegerField(blank=True, null=True)
    elev_min = models.IntegerField(blank=True, null=True)
    elev_5 = models.IntegerField(blank=True, null=True)
    elev_10 = models.IntegerField(blank=True, null=True)
    elev_15 = models.IntegerField(blank=True, null=True)
    elev_20 = models.IntegerField(blank=True, null=True)
    elev_25 = models.IntegerField(blank=True, null=True)
    elev_30 = models.IntegerField(blank=True, null=True)
    elev_35 = models.IntegerField(blank=True, null=True)
    elev_40 = models.IntegerField(blank=True, null=True)
    elev_45 = models.IntegerField(blank=True, null=True)
    elev_med = models.IntegerField(blank=True, null=True)
    elev_55 = models.IntegerField(blank=True, null=True)
    elev_60 = models.IntegerField(blank=True, null=True)
    elev_65 = models.IntegerField(blank=True, null=True)
    elev_70 = models.IntegerField(blank=True, null=True)
    elev_75 = models.IntegerField(blank=True, null=True)
    elev_80 = models.IntegerField(blank=True, null=True)
    elev_85 = models.IntegerField(blank=True, null=True)
    elev_90 = models.IntegerField(blank=True, null=True)
    elev_95 = models.IntegerField(blank=True, null=True)
    elev_max = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'moderncenterlines_hypsometry'


class ModerncenterlinesTopology(models.Model):
    gid = models.AutoField(primary_key=True)
    glimsid = models.CharField(max_length=254, blank=True, null=True)
    branch_tot = models.IntegerField(blank=True, null=True)
    len_90 = models.IntegerField(blank=True, null=True)
    len_80 = models.IntegerField(blank=True, null=True)
    len_70 = models.IntegerField(blank=True, null=True)
    len_60 = models.IntegerField(blank=True, null=True)
    len_50 = models.IntegerField(blank=True, null=True)
    len_40 = models.IntegerField(blank=True, null=True)
    len_30 = models.IntegerField(blank=True, null=True)
    len_20 = models.IntegerField(blank=True, null=True)
    len_10 = models.IntegerField(blank=True, null=True)
    len_0 = models.IntegerField(blank=True, null=True)
    r_20 = models.IntegerField(blank=True, null=True)
    r_30 = models.IntegerField(blank=True, null=True)
    r_40 = models.IntegerField(blank=True, null=True)
    r_50 = models.IntegerField(blank=True, null=True)
    r_60 = models.IntegerField(blank=True, null=True)
    r_70 = models.IntegerField(blank=True, null=True)
    r_75 = models.IntegerField(blank=True, null=True)
    r_80 = models.IntegerField(blank=True, null=True)
    r_85 = models.IntegerField(blank=True, null=True)
    r_90 = models.IntegerField(blank=True, null=True)
    r_95 = models.IntegerField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'moderncenterlines_topology'


class ModernerrorAnalysis(models.Model):
    gid = models.AutoField(primary_key=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    k = models.SmallIntegerField(blank=True, null=True)
    e1 = models.FloatField(blank=True, null=True)
    p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    error = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    errorcat = models.SmallIntegerField(blank=True, null=True)
    id = models.SmallIntegerField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modernerror_analysis'


class Modernoutlinetype(models.Model):
    gid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modernoutlinetype'


class PointBalances(models.Model):
    gid = models.AutoField(primary_key=True)
    rid = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    stake = models.CharField(max_length=254, blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    error = models.FloatField(blank=True, null=True)
    season = models.CharField(max_length=254, blank=True, null=True)
    strata = models.CharField(max_length=254, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    source = models.CharField(max_length=254, blank=True, null=True)
    notes = models.CharField(max_length=250, blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'point_balances'


# class Prism(models.Model):
#     gid = models.AutoField(primary_key=True)
#     date = models.DateField(blank=True, null=True)
#     x = models.FloatField(blank=True, null=True)
#     y = models.FloatField(blank=True, null=True)
#     temperature = models.FloatField(blank=True, null=True)
#     precipitation = models.FloatField(blank=True, null=True)
#     geom = gis_models.GeometryField(blank=True, null=True)
#     lat = models.FloatField(blank=True, null=True)
#     lon = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'prism'


class Snowdepths(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    stakename = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    dens_snow = models.FloatField(blank=True, null=True)
    weq = models.FloatField(blank=True, null=True)
    source = models.CharField(max_length=500, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)
    gid = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'snowdepths'


class Snowradar(models.Model):
    elev = models.FloatField(blank=True, null=True)
    twtt = models.FloatField(blank=True, null=True)
    thickness = models.FloatField(blank=True, null=True)
    swe = models.FloatField(blank=True, null=True)
    trace = models.IntegerField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'snowradar'


class SnowradarLines(models.Model):
    collection = models.TextField(blank=True, null=True)
    velocity = models.FloatField(blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    obs_type = models.TextField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)
    gid = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'snowradar_lines'


# class SnowradarOld(models.Model):
#     elev = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
#     twtt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
#     thickness = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
#     swe = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
#     geom = gis_models.GeometryField(blank=True, null=True)
#     trace = models.IntegerField(blank=True, null=True)
#     gid = models.AutoField(primary_key=True)
#
#     class Meta:
#         managed = True
#         db_table = 'snowradar_old'


class StreamgaugeData(models.Model):
    pkey = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    discharge = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=500, blank=True, null=True)
    gaugeid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'streamgauge_data'


class Streamgauges(models.Model):
    gid = models.AutoField(primary_key=True)
    gaugeid = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    slope = models.IntegerField(blank=True, null=True)
    length = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    elvation = models.IntegerField(blank=True, null=True)
    lake = models.IntegerField(blank=True, null=True)
    forest = models.IntegerField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)
    drainage_area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'streamgauges'


# class SweingestLines(models.Model):
#     collection = models.TextField(blank=True, null=True)
#     geom = gis_models.GeometryField(blank=True, null=True)
#     gid = models.AutoField(primary_key=True)
#
#     class Meta:
#         managed = True
#         db_table = 'sweingest_lines'


# class SweingestMetadata(models.Model):
#     collection = models.TextField(blank=True, null=True)
#     velocity = models.FloatField(blank=True, null=True)
#     density = models.FloatField(blank=True, null=True)
#     date = models.DateField(blank=True, null=True)
#     obs_type = models.TextField(blank=True, null=True)
#     geom = gis_models.GeometryField(blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'sweingest_metadata'


class Velocities(models.Model):
    name = models.TextField(blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    velocity = models.FloatField(blank=True, null=True)
    bearing = models.FloatField(blank=True, null=True)
    start_elevation = models.FloatField(blank=True, null=True)
    end_elevation = models.FloatField(blank=True, null=True)
    start_horizontal_error = models.FloatField(blank=True, null=True)
    end_horizontal_error = models.FloatField(blank=True, null=True)
    error_notes = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)
    gid = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'velocities'


class WeatherstationData(models.Model):
    pkey = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=500)
    date = models.DateTimeField(blank=True, null=True)
    air_temperature = models.FloatField(blank=True, null=True)
    air_pressure = models.FloatField(blank=True, null=True)
    relative_humidity = models.FloatField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    gust_speed = models.FloatField(blank=True, null=True)
    wind_direction = models.FloatField(blank=True, null=True)
    solar_radiation_in = models.FloatField(blank=True, null=True)
    solar_radiation_out = models.FloatField(blank=True, null=True)
    snow_depth = models.FloatField(blank=True, null=True)
    rainfall = models.FloatField(blank=True, null=True)
    battery_voltage = models.FloatField(blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    extension = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'weatherstation_data'


class Weatherstations(models.Model):
    gid = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=254, blank=True, null=True)
    glacier_name = models.CharField(max_length=254, blank=True, null=True)
    station_id = models.CharField(max_length=254, blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    design = models.CharField(max_length=254, blank=True, null=True)
    notes = models.CharField(max_length=254, blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)
    sensor_height = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'weatherstations'
