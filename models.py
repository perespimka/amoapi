# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlertSettings(models.Model):
    device_id = models.CharField(max_length=45)
    metric = models.CharField(max_length=255, blank=True, null=True)
    metric_name = models.CharField(max_length=255, blank=True, null=True)
    yellow_int_1 = models.IntegerField(blank=True, null=True)
    yellow_int_2 = models.IntegerField(blank=True, null=True)
    yellow_time = models.IntegerField(blank=True, null=True)
    yellow_time_now = models.IntegerField(blank=True, null=True)
    red_int = models.IntegerField(blank=True, null=True)
    red_time = models.IntegerField(blank=True, null=True)
    red_time_now = models.IntegerField(blank=True, null=True)
    email = models.IntegerField(blank=True, null=True)
    sms = models.IntegerField(blank=True, null=True)
    slack = models.IntegerField(blank=True, null=True)
    telegram = models.IntegerField(blank=True, null=True)
    email_is_sent = models.IntegerField(blank=True, null=True)
    sms_is_sent = models.IntegerField(blank=True, null=True)
    slack_is_sent = models.IntegerField(blank=True, null=True)
    telegram_is_sent = models.IntegerField(blank=True, null=True)
    notify_is_sent = models.IntegerField(blank=True, null=True)
    notify_id = models.CharField(max_length=20, blank=True, null=True)
    unit = models.CharField(max_length=5, blank=True, null=True)
    metric_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert_settings'


class Balance(models.Model):
    id = models.BigAutoField(unique=True)
    id_user = models.TextField()
    current = models.TextField()
    history = models.TextField()

    class Meta:
        managed = False
        db_table = 'balance'


class DashboardData(models.Model):
    dashboard_id = models.CharField(max_length=45, blank=True, null=True)
    widget_name = models.CharField(max_length=45, blank=True, null=True)
    device_id = models.CharField(max_length=45, blank=True, null=True)
    widget_state = models.CharField(max_length=45, blank=True, null=True)
    widget_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_data'


class Dashboards(models.Model):
    user_id = models.CharField(max_length=45, blank=True, null=True)
    dashboard_id = models.CharField(max_length=45, blank=True, null=True)
    dashboard_type = models.CharField(max_length=45, blank=True, null=True)
    dashboard_name = models.CharField(max_length=45, blank=True, null=True)
    dash_columns = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboards'


class Data(models.Model):
    machine_id = models.CharField(max_length=40)
    cpu = models.TextField(blank=True, null=True)
    cpu1 = models.TextField(blank=True, null=True)
    cpu2 = models.TextField(blank=True, null=True)
    cpu3 = models.TextField(blank=True, null=True)
    cpu4 = models.TextField(blank=True, null=True)
    cpu5 = models.TextField(blank=True, null=True)
    cpu6 = models.TextField(blank=True, null=True)
    cpu7 = models.TextField(blank=True, null=True)
    cpu8 = models.TextField(blank=True, null=True)
    cpu9 = models.TextField(blank=True, null=True)
    cpu10 = models.TextField(blank=True, null=True)
    cpu11 = models.TextField(blank=True, null=True)
    cpu12 = models.TextField(blank=True, null=True)
    cpu13 = models.TextField(blank=True, null=True)
    cpu14 = models.TextField(blank=True, null=True)
    cpu15 = models.TextField(blank=True, null=True)
    cpu16 = models.TextField(blank=True, null=True)
    hdd1 = models.TextField(blank=True, null=True)
    hdd2 = models.TextField(blank=True, null=True)
    hdd3 = models.TextField(blank=True, null=True)
    hdd4 = models.TextField(blank=True, null=True)
    hdd5 = models.TextField(blank=True, null=True)
    hdd6 = models.TextField(blank=True, null=True)
    hdd7 = models.TextField(blank=True, null=True)
    hdd8 = models.TextField(blank=True, null=True)
    dwmemoryload = models.TextField(db_column='dwMemoryLoad')  # Field name made lowercase.
    net1 = models.TextField(blank=True, null=True)
    net2 = models.TextField(blank=True, null=True)
    net3 = models.TextField(blank=True, null=True)
    net4 = models.TextField(blank=True, null=True)
    net5 = models.TextField(blank=True, null=True)
    net6 = models.TextField(blank=True, null=True)
    net7 = models.TextField(blank=True, null=True)
    net8 = models.TextField(blank=True, null=True)
    net9 = models.TextField(blank=True, null=True)
    net10 = models.TextField(blank=True, null=True)
    net11 = models.TextField(blank=True, null=True)
    net12 = models.TextField(blank=True, null=True)
    net13 = models.TextField(blank=True, null=True)
    net14 = models.TextField(blank=True, null=True)
    net15 = models.TextField(blank=True, null=True)
    net16 = models.TextField(blank=True, null=True)
    data_add = models.TextField()

    class Meta:
        managed = False
        db_table = 'data'


class DeviceStatus(models.Model):
    device_id = models.CharField(max_length=45, blank=True, null=True)
    device_name = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    cpu = models.CharField(max_length=45, blank=True, null=True)
    ram = models.CharField(max_length=45, blank=True, null=True)
    date_add = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_status'


class Devices(models.Model):
    id = models.BigAutoField(unique=True)
    device_id = models.CharField(unique=True, max_length=40)
    user_id = models.TextField(blank=True, null=True)
    user_group = models.IntegerField(blank=True, null=True)
    icon = models.CharField(max_length=10, blank=True, null=True)
    device_config = models.TextField(blank=True, null=True)  # This field type is a guess.
    ip = models.TextField(blank=True, null=True)
    date_add = models.IntegerField(blank=True, null=True)
    date_del = models.IntegerField(blank=True, null=True)
    last_connect = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    alias = models.CharField(max_length=45, blank=True, null=True)
    device_group = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices'


class DevicesArchiveData(models.Model):
    id = models.AutoField()
    device_id = models.CharField(max_length=40)
    load_data = models.TextField()  # This field type is a guess.
    date_add = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'devices_archive_data'


class DevicesLiveData(models.Model):
    id = models.AutoField()
    device_id = models.CharField(max_length=40)
    load_data = models.TextField()  # This field type is a guess.
    date_add = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'devices_live_data'


class DevicesWidgetsData(models.Model):
    data = models.TextField(blank=True, null=True)  # This field type is a guess.
    device_id = models.CharField(unique=True, max_length=45, blank=True, null=True)
    device_status = models.CharField(max_length=45, blank=True, null=True)
    date_add = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices_widgets_data'


class GitlabBuilds(models.Model):
    build_id = models.CharField(max_length=45, blank=True, null=True)
    message_id = models.CharField(max_length=45, blank=True, null=True)
    job_name = models.CharField(max_length=45, blank=True, null=True)
    date_add = models.CharField(max_length=45, blank=True, null=True)
    comment = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gitlab_builds'


class Groups(models.Model):
    id = models.BigAutoField(unique=True)
    id_user = models.TextField()
    naim = models.TextField()
    comment = models.TextField()
    data_add = models.TextField()
    del_field = models.TextField(db_column='del')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'groups'


class IpTable(models.Model):
    ip_start = models.TextField()
    ip_end = models.TextField()
    ip_long_from = models.TextField()
    ip_long_to = models.TextField()
    short_country = models.TextField()
    country = models.TextField()

    class Meta:
        managed = False
        db_table = 'ip_table'


class Log(models.Model):
    id = models.BigAutoField(unique=True)
    id_user = models.TextField()
    action = models.TextField()
    data = models.TextField()
    ip = models.TextField()
    http_client = models.TextField()
    timestamp = models.TextField()

    class Meta:
        managed = False
        db_table = 'log'


class MainLog(models.Model):
    id = models.BigAutoField(unique=True)
    machine_id = models.TextField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_log'


class MainMenu(models.Model):
    user_group = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    dest = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    children = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_menu'


class Messages(models.Model):
    id = models.BigAutoField(unique=True)
    user_from = models.TextField()
    user_to = models.TextField()
    text = models.TextField()
    status = models.TextField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'messages'


class Notify(models.Model):
    id = models.BigAutoField(unique=True)
    notify_id = models.TextField(blank=True, null=True)
    user_id = models.TextField()
    notify_level = models.TextField(blank=True, null=True)
    device_id = models.TextField()
    text = models.TextField()
    is_active = models.IntegerField(blank=True, null=True)
    status = models.TextField()
    date_add = models.TextField()

    class Meta:
        managed = False
        db_table = 'notify'


class Roles(models.Model):
    id = models.BigAutoField(unique=True)
    naim = models.TextField()

    class Meta:
        managed = False
        db_table = 'roles'


class Settings(models.Model):
    id = models.BigAutoField(unique=True)
    log_period = models.TextField()
    time_session = models.TextField()
    period_backup = models.TextField()
    last_backup = models.TextField()
    period_del_backup = models.TextField()
    sms_api_id = models.TextField()
    template_sms_offline = models.TextField()
    template_email_offline = models.TextField()
    template_sms_cpu = models.TextField()
    template_email_cpu = models.TextField()
    template_sms_memory = models.TextField()
    template_email_memory = models.TextField()
    template_sms_hdd = models.TextField()
    template_email_hdd = models.TextField()
    template_sms_net = models.TextField()
    template_email_net = models.TextField()
    template_sms_logical = models.TextField()
    template_email_logical = models.TextField()
    balance_naim = models.TextField()
    current_version_exe = models.TextField()
    link_exe = models.TextField()

    class Meta:
        managed = False
        db_table = 'settings'


class UserGroups(models.Model):
    id = models.BigAutoField(unique=True)
    naim = models.TextField()
    roles = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_groups'


class Users(models.Model):
    id = models.BigAutoField(unique=True)
    name = models.TextField(blank=True, null=True)
    login = models.TextField()
    password = models.TextField()
    grp = models.TextField(blank=True, null=True)
    last_enter = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    data_insert = models.TextField(blank=True, null=True)
    del_field = models.TextField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    sended = models.TextField(blank=True, null=True)
    sended_ready = models.TextField(blank=True, null=True)
    key_value = models.TextField(blank=True, null=True)
    uniqid = models.TextField(blank=True, null=True)
    chatid = models.CharField(max_length=45, blank=True, null=True)
    tg_code = models.CharField(max_length=45, blank=True, null=True)
    slack_api = models.TextField(blank=True, null=True)
    slack_channel = models.TextField(blank=True, null=True)
    gitlab_secret = models.CharField(max_length=45, blank=True, null=True)
    gitlab_url = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class WayAdd(models.Model):
    id = models.BigAutoField(unique=True)
    naim = models.TextField()
    picture = models.TextField()
    alias = models.TextField()
    details = models.TextField()

    class Meta:
        managed = False
        db_table = 'way_add'
