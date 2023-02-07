from django.db import models

# Create your models here.
class TrainerModel(models.Model):
    empid=models.CharField(max_length=15,primary_key=True)
    name=models.CharField(max_length=40)
    experience=models.PositiveIntegerField()
    date_of_join=models.DateField()
    salary=models.PositiveIntegerField()
    subject=models.CharField(max_length=30)


