from django.db import models

# Create your models here.
class Home(models.Model):
    winner = models.CharField(max_length=20)
    wpts = models.IntegerField()
    loser = models.CharField(max_length=20)
    lpts = models.IntegerField()


class Comment(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey('Home', on_delete=models.CASCADE)