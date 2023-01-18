#!/usr/bin/env python3
import re

# The song lyrics should match the pattern "[Verse X] some lyrics", where X is a number, and "some lyrics" can be any string of characters.
song_pattern = re.compile(r"\[Verse [0-9]+\] .+")

# Function to find song lyrics in a string:
def find_songs(string):
    songs = song_pattern.findall(string)
    if songs:
        return 'Song lyrics found: ' + ', '.join(songs)
    else:
        return 'No song lyrics found.'

# Test the function:
print(find_songs("[Verse 1] I'm singing in the rain, just singing in the rain. [Verse 2] What a glorious feeling, I'm happy again."))
print(find_songs("[Verse 1] I'm singing in the rain, just singing in the rain. [Verse 2] What a glorious feeling, I'm happy again. [Verse 3] I'm laughing at clouds, so dark up above. [Verse 4] The sun's in my heart, and I'm ready for love."))