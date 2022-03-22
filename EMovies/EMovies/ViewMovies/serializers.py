from rest_framework import serializers
from .models import City,Theater,Movies

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields=['city_name']

class TheaterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields=['Theater_name']

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields=['movie_id','movie_name','city_id','theater_id','screen_id','release_date']
