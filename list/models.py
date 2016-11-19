from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=1000)
    roll_num = models.CharField(max_length=1000,primary_key=True)
    aggregate = models.FloatField(default=None)

    def __str__(self):
        return("Name:"+self.name+" Enrollment Number:"+str(self.roll_num)+" Aggregate:"+str(self.aggregate))
