from django.db import models
from django.urls import reverse


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    course = models.CharField(max_length=100)


    #
    # def get_absolute_url(self):
    #     return reverse("contact")
