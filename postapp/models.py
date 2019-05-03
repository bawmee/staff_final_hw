from django.db import models
from django.utils import timezone


class post(models.Model):
    site = models.CharField(max_length = 20, null = False, default = "입력없음")
    contry = models.CharField(max_length = 50)
    genre = models.CharField(max_length = 20)
    title = models.CharField(max_length = 50)
    rate = models.IntegerField(null = False)
    review = models.TextField(null = False, default = "입력없음")
    date = models.DateTimeField('date published', default=timezone.now)
    writer = models.CharField(max_length = 20 , default="gyuzizi")

    def summary(self):
        return self.review[:20]



class com(models.Model):
    post = models.ForeignKey('postapp.post', related_name='coms', on_delete=models.CASCADE)
    content = models.TextField(default = "내용없음")
    writer = models.CharField(max_length=20, default="gyuzizi")
    date = models.DateTimeField(default=timezone.now)