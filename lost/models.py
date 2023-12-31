from django.db import models


# Create your models here.

# User table
class User(models.Model):

    username = models.CharField(max_length=20)

    password = models.CharField(max_length=20)


# List of lost property
class Lost(models.Model):
    Location = models.CharField(max_length=20)
    Date = models.DateField()
    Category = models.CharField(max_length=20)
    # optional enter
    UPass = models.CharField(max_length=20,null=True)
    Description = models.CharField(max_length=200)


# Announcement list
class Notice(models.Model):
    Content = models.CharField(max_length=200)
    userid = models.CharField(max_length=20)
