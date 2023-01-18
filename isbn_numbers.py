#!/usr/bin/env python3
import re

# The ISBN numbers should match the pattern "ISBN xxx-x-xxx-xxxxx-x", where x is a digit.
isbn_pattern = re.compile(r"ISBN [0-9]{3}-[0-9]-[0-9]{3}-[0-9]{5}-[0-9]")

# Function to find ISBN numbers in a string:
def find_isbn(string):
    isbn = isbn_pattern.findall(string)
    if isbn:
        return 'ISBN number(s) found: ' + ', '.join(isbn)
    else:
        return 'No ISBN number found.'

# Test the function:
print(find_isbn("Lorem, Ipsum! ISBN number is ISBN 123-4-567-89012-3"))
print(find_isbn("Lorem, Ipsum! ISBN number is 123-4-567-89012-3"))