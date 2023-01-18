#!/usr/bin/env python3
import re

# The hex color codes should match the pattern "#XXXXXX" where X is any letter or digit.
hex_pattern = re.compile(r"#[a-fA-F0-9]{6}")

# Function to find hex color codes in a string:
def find_hex(string):
    hex = hex_pattern.findall(string)
    if hex:
        return 'Hex color code(s) found: ' + ', '.join(hex)
    else:
        return 'No hex color code found.'

# Test the function:
print(find_hex("The color of the sky is #87CEEB. The color of the grass is #3CB371"))
print(find_hex("The color of the sky is #87CEEB. The color of the grass is #33333. The color of the water is #0000FF"))