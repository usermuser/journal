# coding: utf-8

from django.db import models
from django.contrib.auth.models import User

class Cpu(models.Model):
    name=models.CharField(max_length=75)
    ip=models.CharField(max_length=16)
    zone=models.CharField(max_length=75)
    
    def __unicode__(self):
        return self.name

class Pda(models.Model):
    cpu=models.ForeignKey(Cpu)
    text=models.TextField(max_length=300)
    date=models.DateTimeField(auto_now=True)
    #file=models.FileField(upload_to=)
    user = models.ForeignKey(User,)
    
    def __unicode__(self):
        return unicode(self.date)
