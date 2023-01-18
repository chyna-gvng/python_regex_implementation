#!/usr/bin/env python3
import re

# The IP addresses should match the pattern "xxx.xxx.xxx.xxx" where x is a digit between 0 and 255.
ip_pattern = re.compile(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")

# Function to find IP addresses in a string:
def find_ip(string):
    ip = ip_pattern.findall(string)
    if ip:
        return 'IP address(es) found: ' + ', '.join(ip)
    else:
        return 'No IP address found.'

# Test the function:
print(find_ip("Hello, world! IP address is 192.168.1.1 "))
print(find_ip("Hello, world! IP address is 2899.45550.06666.666661"))