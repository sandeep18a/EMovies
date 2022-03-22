from django.urls import path
from ViewMovies import views

urlpatterns = [
    path('city/', views.CityList),
    path('movies/',views.MovieList),
    path('movieByCity/',views.MovieByCity),
    path('editMovieDetails/<pk>',views.EditMovieDetail)

    # path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # path(r'^api/tutorials/published$', views.tutorial_list_published)
]