from django.shortcuts import render
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import City,Movies
from .serializers import CitySerializers,MoviesSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def CityList(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials

    if request.method == 'GET':
        cities = City.objects.all()

        city_name = request.GET.get('city_name', None)
        if city_name is not None:
            cities = cities.filter(city__icontains=city_name)

        city_serializer = CitySerializers(cities, many=True)
        return JsonResponse(city_serializer.data, safe=False)

    elif request.method == 'POST':
        city_data = JSONParser().parse(request)
        city_serializer = CitySerializers(data=city_data)
        if city_serializer.is_valid():
            city_serializer.save()
            return JsonResponse(city_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(city_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST', 'DELETE'])
def MovieList(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials

    if request.method == 'GET':
        movies = Movies.objects.all()
        city=Movies.city_id

        movie_name = request.GET.get('movie_name', None)
        if movie_name is not None:
            movies = movies.filter(movies__icontains=city)

        movie_serializer = MoviesSerializer(movies, many=True)
        return JsonResponse(movie_serializer.data, safe=False)

    elif request.method == 'POST':
        movies_data = JSONParser().parse(request)
        movie_serializer = MoviesSerializer(data=movies_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(movie_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def MovieByCity(request):
        if request.method == 'GET':
            movies = Movies.objects.all()

            city_id = request.GET.get('city_id', None)
            if city_id is not None:
                movies = movies.filter(city_id=city_id)

            movies_serializer = MoviesSerializer(movies, many=True)
            return JsonResponse(movies_serializer.data, safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
def EditMovieDetail(request,pk):
    movie = Movies.objects.get(pk=pk)
    if request.method == 'PUT':
        movies_data = JSONParser().parse(request)
        movies_serializer = MoviesSerializer(movie, data=movies_data)
        if movies_serializer.is_valid():
            movies_serializer.save()
            return JsonResponse(movies_serializer.data)
        return JsonResponse(movies_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
