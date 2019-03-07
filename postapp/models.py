from django.db import models

# Create your models here.


class post(models.Model):
    site = models.CharField(null = False)
    contry = models.CharField()
    genre = models.CharField()
    title = models.CharField()
    rate = models.IntegerField(null = False)
    review = models.TextField(max_length = 200, null = False)
    date = models.DateTimeField('date published')
    writer = models.CharField()