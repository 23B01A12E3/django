from django.db import models

class Student(models.Model):
    stname = models.CharField(max_length=100)
    stage = models.IntegerField()
    stemail = models.EmailField()
