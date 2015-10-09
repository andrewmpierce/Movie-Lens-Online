from django.db import models
from django.contrib.auth.models import User

class Rater(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    X = 'X'

    user = models.OneToOneField(User, primary_key=True)
    genders = ((MALE, 'Male'), (FEMALE, 'Female'), (OTHER, 'Other'), (X, 'X'))
    rater_id = models.PositiveSmallIntegerField()
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1, choices=genders, default='X')
    zipcode = models.PositiveSmallIntegerField()
    occupation = models.CharField(max_length=50)



class Movie(models.Model):
    title = models.CharField(max_length=255)
    movie_id = models.PositiveSmallIntegerField(primary_key=True)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']



class Rating(models.Model):
    rater = models.ForeignKey('Rater')
    movie = models.ForeignKey('Movie')
    stars = models.PositiveSmallIntegerField()
