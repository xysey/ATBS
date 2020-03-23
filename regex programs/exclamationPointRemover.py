#! python3
'''
A program to search and remove repeated exclamation points.
'''
import re
import pyperclip

text = str(pyperclip.paste())
# will search a for a repeated exclamation mark
exclamationRegex = re.compile(r'\b(!{2,})')
#remove the excess exclamation mark
if exclamationRegex.search(text):
    text = exclamationRegex.sub(r'!', text)
#copy to clipboard
    print("Excess exclamation mark removed. Copied the new text to the clipboard.")
    pyperclip.copy(text)
else:
    print("No repeated exclamation mark found.")
