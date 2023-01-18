#!/usr/bin/env python3
import re

# The movie titles should match the pattern "Title (yyyy)", where "Title" is any string of characters, and "yyyy" is a four-digit year.
movie_pattern = re.compile(r"Title \([0-9]{4}\)")

# Function to find movie titles in a string:

def find_movies(string):
    movies = movie_pattern.findall(string)
    if movies:
        return 'Movie title(s) found: ' + ', '.join(movies)
    else:
        return 'No movie title found.'

# Test the function:
print(find_movies("Title (2022)"))
print(find_movies("Kaleidoscope (2022) and ALU (2023)"))