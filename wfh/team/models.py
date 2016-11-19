from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


from django.utils import timezone
from django.utils.text import slugify

from django.core.urlresolvers import  reverse
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.

class TeamMember(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	teamName = models.CharField(max_length=120)
	designation = models.CharField(max_length=150,blank=True)
	grade = models.CharField(max_length=50,blank=True)
	email = models.EmailField(max_length=50)
	phone = models.IntegerField(max_length=10, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])  
	
	def __unicode__(self):
		return self.user.get_username()

	def __str__(self):
		return self.user.get_username()

	class Meta:
		ordering =["grade"]  