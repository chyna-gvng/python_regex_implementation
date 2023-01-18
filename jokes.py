#!/usr/bin/env python3
import re

# The jokes should match the pattern "Why did the ... ? Because...", where the first part of the pattern can be any string of characters, and the second part can be any string of characters.
jokes_pattern = re.compile(r"Why did the .+\? .+")

# Function to find jokes in a string:

def find_jokes(string):
    jokes = jokes_pattern.findall(string)
    if jokes:
        return 'Jokes found: ' + ', '.join(jokes)
    else:
        return 'No jokes found.'

# Test the function:
print(find_jokes("Why did the tomato turn red? Because it saw the salad dressing! Why did the chicken cross the road? To get to the other side!"))
print(find_jokes("Why did the cow jump over the moon?"))