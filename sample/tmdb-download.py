#!/usr/bin/env python

import os
import sys
import tmdb
import json
import argparse

parser = argparse.ArgumentParser(prog='./tmdb-download.py', description='Download all movie titles for a list of years from themoviedb.org')
parser.add_argument('years', nargs='+', type=int, help='A list of years space-separated')
parser.add_argument('directory', type=str, default='.', help='Directory to store movie titles in')
args = parser.parse_args()

def read_file(filename):
  return open(filename).read()

def search_movies(keyword, year):
  yearMovies = tmdb.Movies('%s&year=%s'%(str(keyword),str(year)))
  return [movie['id'] for movie in yearMovies.iter_results()]

def search_movies_for_year(year):
  movieIds = set()
  for keyword in ['a','e','i','o','u']:
    movieIds.update(search_movies(keyword, year))
  movies = []
  for movieId in movieIds:
    try:
      movies.append(tmdb.Movie(movieId).movies)
    except:
      continue
  return movies

api_key = read_file('themoviedb_apikey').strip()
tmdb.configure(api_key)

downloads_directory = args.directory
years = args.years

if not os.path.isdir(downloads_directory):
  print >> sys.stderr, 'Downloads directory %s does not exist'
  sys.exit(1)

year_directory = lambda year : os.path.join(downloads_directory, str(year))

for year in years:
  yearMovies = search_movies_for_year(year)
  print year, len(yearMovies)
  
  movie_filename = lambda year, n : year_directory(year) + '/%06d.json' % (n)
  
  os.mkdir(year_directory(year))
  for i, movie in enumerate(yearMovies):
    with open(movie_filename(year, i), 'w') as outfile:
      json.dump(movie, outfile)

