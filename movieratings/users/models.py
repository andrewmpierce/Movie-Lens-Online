from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, null=True)
    favorite_color = models.CharField(max_length=50)
