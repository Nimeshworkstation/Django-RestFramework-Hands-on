from django.db import models

class Student(models.Model):
	name = models.CharField(max_length = 70)
	city = models.CharField(max_length = 100)
	roll = models.IntegerField()

#Creating Signals
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#This Signal Creates AuthToken for Users
@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created = False, **kwargs):
	if created:
		Token.objects.create(user=instance)