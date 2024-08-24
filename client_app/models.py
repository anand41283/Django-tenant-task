from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
