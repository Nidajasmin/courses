from django.db import models

# Create your models here.
class Courses(models.Model):
    tile=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    seats=models.IntegerField(max_length=100)
    fee=models.IntegerField(max_length=100)
    image=models.ImageField(upload_to='image',null=True) 

    def __str__(self):
        return self.tile