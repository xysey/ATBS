#! python3
"""
A program to search and remove repeated words.
"""
import re, pyperclip

text = str(pyperclip.paste())
spaceRegex = re.compile(
    r"(\b\S+\b)\s+\b\1\b", re.I
)  # will search a for a repeated word(1)
# remove the excess word(s)
if spaceRegex.search(text):
    text = spaceRegex.sub(r"\1", text)
    # copy to clipboard
    print("Excess word(s) removed. Copied the new text to the clipboard.")
    pyperclip.copy(text)
else:
    print("No repeated word found.")
