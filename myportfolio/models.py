from django.db import models


class Case(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    site_url = models.URLField(max_length=1024)
    repo_url = models.URLField(max_length=1024)
    image = models.ImageField(upload_to='repo')


class About(models.Model):
    title = models.CharField(max_length=255, null=False)
    text = models.CharField(max_length=512)


class Skill(models.Model):
    title = models.CharField(max_length=255, null=False)
    test = models.TextField(null=False)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    url = models.CharField(max_length=1024)


class Url(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=1024)