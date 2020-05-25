from django.db import models
from django.urls import reverse
# Create your models here.


class Employee(models.Model):
    EmpID = models.IntegerField(primary_key=True)
    Empname = models.CharField(max_length=40)
    EmpAge = models.IntegerField()
    EmpSal = models.FloatField()
    EmpDesignation = models.CharField(max_length=40)
    Empcity = models.CharField(max_length=40)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})