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
    zipcode = models.CharField(max_length=5)


    def __str__(self):
        return str(self.id)


class Movie(models.Model):
    title = models.CharField(max_length=255)

    #class Meta:
    #    ordering = ['-average_rating']

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']

    def __str__(self):
        return ' Title : {}'.format(self.title)

class Rating(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(Rater)
    stars = models.IntegerField()

    def __str__(self):
        return ' Title : {}, Rating: {}, Rater {}'.format(self.movie, self.stars, self.user)


def get_ratings(movieid, ratings):
    for rating in ratings:
        av_stars = []
        if rating[rating][fields][movie] == movieid:
            rating[rating][fields][stars].append(av_stars)
        return(sum(av_stars)/len(av_stars))



def load_ml_data():
    import csv
    import json
    import re

    users = []

    with open('data/users.dat') as f:

        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='\t')
        for row in reader:
            user = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'ratings.Rater',
                'pk': int(row['UserID']),
            }

            users.append(user)

    with open('fixtures/users.json', 'w') as f:
        f.write(json.dumps(users))

    #print(json.dumps(users, sort_keys=True, indent=4, separators=(',', ': ')))


    ratings = []

    with open('data/ratings.dat') as f:
        count = 1
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::MovieID::Rating::Timestamp'.split('::'),
                                delimiter='\t')
        for row in reader:
            rating = {
                'fields': {
                    'stars': row['Rating'],
                    'user': row['UserID'],
                    'movie': row['MovieID']
                },
                'model': 'ratings.Rating',
                'pk': count
            }

            ratings.append(rating)
            count += 1

    with open('ratings.json', 'w') as f:
        f.write(json.dumps(ratings))


    movies = []

    with open('data/movies.dat', encoding='windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genres'.split('::'),
                                delimiter='\t')
        for row in reader:
            movie = {
                'fields': {
                    'title': row['Title']
                },
                'model': 'ratings.Movie',
                'pk': int(row['MovieID'])
            }

            movies.append(movie)

    with open('movies.json', 'w') as f:
        f.write(json.dumps(movies))

def delete_extra_data():
    for movie in Movie.objects.all():
        if movie.average_rating is None:
            movie.delete()
