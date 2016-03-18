from django.db import models


class Tablature(models.Model):
    song = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    tab_type = models.CharField(max_length=10)
    tab = models.TextField()
