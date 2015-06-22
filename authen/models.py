from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    balance = models.FloatField(default=0.0)
    picture = models.ImageField(upload_to='static/user_img', blank=True)
