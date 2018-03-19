# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	language = models.TextField()
	updated_on = models.DurationField()
	
	class Meta:
		ordering = ['title']

                def __unicode__(self):
                        return self.title
