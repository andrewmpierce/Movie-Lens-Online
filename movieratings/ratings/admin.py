from django.contrib import admin
from .models import Status, Favorite


class RaterAdmin(admin.ModelAdmin):
    #list_display = []
    pass

class MoviesAdmin(admin.ModelAdmin):
    #list_display = ['user', 'status']
    pass

class RatingsAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Rater, RaterAdmin)
admin.site.register(Movies, MoviesAdmin)
admin.site.register(Ratings, RatingsAdmin)
