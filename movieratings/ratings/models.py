from django.db import models


class Rater(models.Model):
    age = models.IntegerField()
    occupation = models.CharField(max_length=50)

    def __str__(self):
        return ' Age : {}, Occupation:{}'.format(self.age, self.occupation)


class Movie(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return ' Title : {}, Stars: {}'.format(self.title, self.stars)


class Rating(models.Model):
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()

    def __str__(self):
        return ' Title : {}, Rating: {}'.format(self.movie, self.rating)
