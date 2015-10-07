from django.db import models


class Raters(models.Model):
    age = models.IntegerField()
    occupation = models.CharField(max_length=50)

    def __str__(self):
        return ' Age : {}, Occupation:{}'.format(self.age, self.occupation)


class Movies(models.Model):
    title = models.CharField(max_length=100)
    stars = models.ForeignKey(Ratings)
    
    def __str__(self):
        return ' Title : {}'.format(self.title)


class Ratings(models.Model):
    movie = models.ForeignKey(Movies)
    rating = models.IntegerField()

    def __str__(self):
        return ' Title : {}, Rating: {}'.format(self.movie, self.rating)
