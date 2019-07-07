# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Dob(models.Model):
	day = models.IntegerField()
	month = models.CharField(max_length=10)
	year = models.IntegerField()

	def __str__(self):
		return str(self.day)

class User(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)
	age = models.IntegerField()
	# day = models.IntegerField()
	# month = models.CharField(max_length=10, null=False, blank=False)
	# year = models.IntegerField()
	dob = models.ForeignKey(Dob, on_delete=models.CASCADE, null=False)

	def __str__(self):
		return self.name

# class User(models.Model):
# 	name = models.CharField(max_length=50, null=False, blank=False)
# 	age = models.IntegerField()
# 	day = models.IntegerField()
# 	month = models.CharField(max_length=10, null=False, blank=False)
# 	year = models.IntegerField()

# 	def __str__(self):
# 		return self.name

