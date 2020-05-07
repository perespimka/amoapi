from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    owner = models.OneToOneField(User, models.CASCADE)
    chatid = models.CharField(max_length=45, blank=True, null=True)
    tg_code = models.CharField(max_length=45, blank=True, null=True)
    pass_reset_token = models.CharField(max_length=45, blank=True, null=True) #Токен для восстановления пароля