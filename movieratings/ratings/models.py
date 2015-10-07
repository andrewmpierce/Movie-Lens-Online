from django.db import models


class Rater(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    DNR = 'X'
    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'F'),
        (OTHER, 'O'),
        (DNR, 'X'),
        )

    age = models.IntegerField()
    occupation = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='X')

    def __str__(self):
        return ' Age : {}, Occupation:{}'.format(self.age, self.occupation)


class Movie(models.Model):
    title = models.CharField(max_length=100)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('Stars'))['stars__avg']

    def __str__(self):
        return ' Title : {}'.format(self.title)


class Rating(models.Model):
    movie = models.ForeignKey('Movie')
    user = models.ForeignKey('Rater')
    stars = models.IntegerField(default=0)

    def __str__(self):
        return ' Title : {}, Rating: {}, Rater {}'.format(self.movie, self.stars, self.user)
