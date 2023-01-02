from django.db import models


class StudentData(models.Model):
    name = models.CharField(max_length=200)
    grade = models.CharField(max_length=10)
    