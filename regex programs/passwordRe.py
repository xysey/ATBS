#! python3
"""
A function that will tell you if your password is strong according to the requirement in the strong password detection practice project
"""

import re


def isPwStrong(password):
    length = re.search(r"[a-zA-Z0-9]{8,}", password)
    uppercase = re.search(r"[A-Z]", password)
    lowercase = re.search(r"[a-z]", password)
    digit = re.search(r"\d+", password)

    if length == None or uppercase == None or lowercase == None or digit == None:
        return False
    else:
        return True
