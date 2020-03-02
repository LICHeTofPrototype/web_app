from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  class Meta:
    db_table = "custom_user"
    
  SEX_CHOICE = (("M", 'Male'), ("F", 'Female'))
  login_count = models.IntegerField(verbose_name="login_count", default=0)
  which_sex = models.CharField(max_length=1, verbose_name="sex")
  birth_date = models.DateField(verbose_name="birth_date")
  age = models.IntegerField(verbose_name="age")