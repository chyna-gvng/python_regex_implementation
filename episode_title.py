#!/usr/bin/env python3
import re

# The episode titles should match the pattern "Show Name SXXEXX: Episode Title", where "Show Name" is any string of characters, SXX is a two-digit season number and EXX is a two-digit episode number, and "Episode Title" is any string of characters.
episode_pattern = re.compile(r"[a-zA-Z ]+ S[0-9]{2}E[0-9]{2}: .+")

# Function to find episode titles in a string:
def find_episodes(string):
    episodes = episode_pattern.findall(string)
    if episodes:
        return 'Episode title(s) found: ' + ', '.join(episodes)
    else:
        return 'No episode title found.'

# Test the function:
print(find_episodes("The Simpsons S01E01: Simpsons Roasting on an Open Fire. The Simpsons S01E02: Bart the Genius"))
print(find_episodes("The Simpsons S01E01: Simpsons Roasting on an Open Fire. The Simpsons S01E02: Bart the Genius. The Simpsons S01E03: Homer's Odyssey"))