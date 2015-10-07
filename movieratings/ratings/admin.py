from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['age', 'occupation']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'rating']


# Register your models here.
admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
