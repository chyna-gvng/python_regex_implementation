#!/usr/bin/env python3
import re

# The dates should match the pattern dd-MMM-yyyy, where dd is a two-digit day, MMM is a three-letter month abbreviation, and yyyy is a four-digit year.
date_pattern = re.compile(r"[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}")

# Function to find dates in a string:
def find_dates(string):
    dates = date_pattern.findall(string)
    if dates:
        return 'Date(s) found: ' + ', '.join(dates)
    else:
        return 'No date found.'

# Test the function:
print(find_dates("Today is 18-Jan-2023 and tomorrow is 19-Jan-2023"))
print(find_dates("The day after tomorrow is 20-01-2023"))