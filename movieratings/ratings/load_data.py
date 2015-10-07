import csv
from models import Movie

movies = 'movieratings/data/movies.dat'

moviedata = csv.reader(open(movies, delimiter='::', encoding = 'latin_1'))

for row in moviedata:
    movie = Movie()
    movie.id = row[0]
    movie.title = row[1]
