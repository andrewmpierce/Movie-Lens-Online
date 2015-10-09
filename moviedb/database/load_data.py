import csv
import json
from database.models import *
from faker import Faker
import random


def load_movies():
    movies = []

    with open('data/movies.dat', encoding='windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genres'.split('::'),
                                delimiter='\t')

        for row in reader:
            movie = {
            'fields':{
                'title':row['Title']},
            'model':'database.Movie',
            'pk': int(row['MovieID'])
            }
            movies.append(movie)

    with open('movies.json', 'w') as f:
        f.write(json.dumps(movies))

def load_raters():
    raters = []

    with open('data/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='\t')

        for row in reader:
            rater = {
            'fields':{
                'gender':row['Gender'],
                'age': row['Age'],
                'occupation': row['Occupation'],
                'zipcode' : row['Zip-code']},

            'model':'database.Rater',
            'pk': int(row['UserID'])
            }
            raters.append(rater)

    with open('raters.json', 'w') as f:
        f.write(json.dumps(raters))

def load_ratings():
    ratings = []

    with open('data/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::MovieID::Rating::Timestamp'.split('::'),
                                delimiter='\t')
        count = 1
        for row in reader:

            rating = {
            'fields':{
                'rater':int(row['UserID']),
                'movie':row['MovieID'],
                'stars': row['Rating']},

            'model':'database.Rating',
            'pk': count }
            ratings.append(rating)
            count += 1

    with open('ratings.json', 'w') as f:
        f.write(json.dumps(ratings))

def create_users():
    fake = Faker()
    for rater in Rater.objects.all():
        if rater.user == None:
            rater.user = User.objects.create_user(username=fake.user_name()+str(random.randint(1, 999)),
                                email= fake.email(),
                                password='password')
            rater.save()
            print(rater.user.username)
