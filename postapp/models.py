from django.db import models

# Create your models here.


class post(models.Model):
    site = models.CharField(max_length = 20, null = False)
    contry = models.CharField(max_length = 15)
    genre = models.CharField(max_length = 20)
    title = models.CharField(max_length = 20)
    rate = models.IntegerField(null = False)
    review = models.TextField(max_length = 150, null = False)
    date = models.DateTimeField('date published')
    writer = models.CharField(max_length = 20)