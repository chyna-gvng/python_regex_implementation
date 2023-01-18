#!/usr/bin/env python3
import re

# The twitter handles should match the pattern "@username", where "username" can be any string of letters and digits.
twitter_pattern = re.compile(r"@[a-zA-Z0-9]+")

# Function to find twitter handles in a string:
def find_twitter(string):
    twitter = twitter_pattern.findall(string)
    if twitter:
        return 'Twitter handle(s) found: ' + ', '.join(twitter)
    else:
        return 'No twitter handle found.'

# Test the function:
print(find_twitter("Follow me on twitter @Wakuma"))
print(find_twitter("Follow me on twitter Wakuma2"))