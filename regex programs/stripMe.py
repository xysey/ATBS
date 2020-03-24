#! python3
"""
A function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string. And then return stripped string
"""

import re


def stripMe(strings, characters=None):
    if characters == None:
        return re.sub(r"\s*(.*)\b\s*", r"\1", strings)
    else:
        return re.sub(r"[" + characters + "]", "", strings)
