from django.db import models
from django.contrib.auth.models import User

class Rater(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    X = 'X'

    user = models.OneToOneField(User, null=True)
    genders = ((MALE, 'Male'), (FEMALE, 'Female'), (OTHER, 'Other'), (X, 'X'))
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1, choices=genders, default='X')
    zipcode = models.CharField(max_length=15)
    occupation = models.CharField(max_length=50)

    def __str__(self):
         return '{}'.format(self.user)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    movie_id = models.PositiveSmallIntegerField(primary_key=True)

    def __str__(self):
         return '{} {}'.format(self.pk, self.title)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']




class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.PositiveSmallIntegerField()

    def __str__(self):
         return '{} {} {}'.format(self.rater, self.movie, self.stars)
