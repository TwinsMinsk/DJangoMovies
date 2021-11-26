from django.contrib import admin
from .models import Category, Actor, Genre, Movie, Movie_shots, RatingStar, Rating, Review


admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Movie_shots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Review)

