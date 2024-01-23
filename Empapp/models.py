from django.db import models

# Create your models here.
class department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)

class employee(models.Model):
    empid=models.AutoField(primary_key=True)
    empname=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    doj=models.DateField()
    photofilename=models.CharField(max_length=500)

    