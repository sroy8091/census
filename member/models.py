# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Member(models.Model):
    sex = (('Male','Male'), ('Female', 'Female'))
    employ = (('Student', 'Student'), ('Employed', 'Employed'))

    head = models.ForeignKey(User)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    sex = models.CharField(max_length=10, choices=sex)
    employment_satus = models.CharField(max_length=50, choices=employ)
    adhaar_no = models.CharField(max_length=10)
    request_status = models.BooleanField(default=False)