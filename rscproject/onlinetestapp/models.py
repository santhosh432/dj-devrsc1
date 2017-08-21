# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    tech = models.CharField(max_length=20)


'''
class Registrationform(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    emailid = models.CharField(max_length=50)
    mobileno = models.IntegerField()
    dno = models.CharField(max_length=10)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    dist = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    tech = models.CharField(max_length=20)


'''


class Techlist(models.Model):
    subjectname = models.CharField(max_length=30)
    timelimit = models.IntegerField()
    status = models.CharField(max_length=10, default='Deactive')


class Questionslist(models.Model):
    question = models.TextField(max_length=500)
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d = models.CharField(max_length=100)
    ro = models.CharField(max_length=2)
    subtype = models.CharField(max_length=50)


class Empanswerslist(models.Model):
    empid = models.IntegerField()
    empmailid = models.CharField(max_length=50)
    empqueid = models.IntegerField()
    empanswer = models.CharField(max_length=5)
    originalanswer = models.CharField(max_length=5)
    emptech = models.CharField(max_length=20)
    testid = models.IntegerField()

