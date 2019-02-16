from django.db import models

# Create your models here.


class Tutorial(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    p_lang = models.CharField(max_length=50)
    tutorial_logo = models.CharField(max_length=2000)
    t_dir = models.CharField(max_length=2000)
    t_date = models.DateTimeField('Tutorial pub')


class Topic(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file_type = models.CharField(max_length=50)
    vote = models.IntegerField(default=0)

