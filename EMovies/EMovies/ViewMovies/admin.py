from django.contrib import admin
from .models import City,Theater,Screens,Movies
# Register your models here.
admin.site.register(City)
admin.site.register(Theater)
admin.site.register(Screens)
admin.site.register(Movies)