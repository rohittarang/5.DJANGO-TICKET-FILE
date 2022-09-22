from tkinter import CASCADE
from django.db import models

# Create your models here.
class Register(models.Model):
    murole = models.CharField(max_length=20,default="")
    marole = models.CharField(max_length=20,default="")
    musername = models.CharField(max_length=20)
    mpassword = models.CharField(max_length=20)
    
    def __str__(self):
        return self.musername

class Login(models.Model):
    mulrole = models.CharField(max_length=20,default="")
    malrole = models.CharField(max_length=20,default="")
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username

class Ticket(models.Model):
    ticketno = models.CharField(max_length=100,default="")
    serverdetails = models.CharField(max_length=100,default="")
    senddate = models.DateTimeField('created at', auto_now_add=True)
    licenseno = models.CharField(max_length=25, default="")
    mfile = models.FileField(default="")
    
    def __str__(self):
        return self.ticketno
    


