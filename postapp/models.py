from django.db import models

# Create your models here.


class post(models.Model):
    site = models.CharField(max_length = 20, null = False, default = "입력없음")
    contry = models.CharField(max_length = 50)
    genre = models.CharField(max_length = 20)
    title = models.CharField(max_length = 50)
    rate = models.IntegerField(null = False)
    review = models.TextField(max_length = 250, null = False, default = "입력없음")
    date = models.DateTimeField('date published')
    writer = models.CharField(max_length = 20)

    def summary(self):
        return self.review[:20]