from django.db import models

# Create your models here.
class City(models.Model):
    city_id = models.CharField(primary_key=True,),
    city_name=models.CharField(max_length=70)

class Theater(models.Model):
    theater_id=models.CharField(primary_key=True,max_length=10),
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    theater_name=models.CharField(max_length=70)

class Screens(models.Model):
    screen_id = models.CharField(primary_key=True,max_length=10),
    theater_id = models.ForeignKey(Theater, on_delete=models.CASCADE)


class Movies(models.Model):
    movie_id=models.CharField(primary_key=True,max_length=70,default="Mov")
    movie_name=models.CharField(max_length=70)
    city_id =models.ForeignKey(City,on_delete=models.CASCADE)
    theater_id=models.ForeignKey(Theater,on_delete=models.CASCADE)
    screen_id=models.ForeignKey(Screens,on_delete=models.CASCADE)
    release_date=models.DateField(default='')
