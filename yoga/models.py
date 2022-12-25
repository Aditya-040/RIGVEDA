from django.db import models

# Create your models here.


class Yoga(models.Model):
    name = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='yogaimg')
    problem = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name


class userinfo(models.Model):
    username = models.CharField(max_length=80)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    problem = models.CharField(max_length=50)

    def __str__(self):
        return self.username
