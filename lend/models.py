from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    author = models.CharField(max_length=255, blank=False)
    copies = models.IntegerField(blank=False, default=1)
    status = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.name

class Issuebook(models.Model):
    username = models.CharField(max_length=255, blank=False)
    bookname = models.CharField(max_length=255, blank=False)
    groupname = models.CharField(max_length=255, blank=False)
    issued = models.IntegerField(default=0)
    can_issue = models.IntegerField(blank=True)

    def __str__(self):
        return self.username

class usergroups(models.Model):
    username = models.CharField(max_length=255, unique=True, blank=False)
    group = models.CharField(max_length=120, blank=False)

    def __str__(self):
        return self.username
