# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

class UserModel(AbstractUser):
	""" Extending user model for adding 
		extra fields and permission in user model"""
	code = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True,
								   editable=False)
	last_modified = models.DateTimeField(auto_now=True,
										 editable=False)

	class Meta:
		ordering = ('first_name',)
