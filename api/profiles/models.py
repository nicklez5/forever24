from django.db import models
from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    address = models.CharField(max_length=400,null=True,blank=True)
# Create your models here.
