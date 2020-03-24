#! python3
'''
This program searches for excess space in a text from clipboard and deletes it.
Then it will copy it to the clipboard
'''
import re
import pyperclip
text = str(pyperclip.paste())
spaceRegex = re.compile(r'[ ]{2,}')  # will search a double space or more
# search for space in a text and delete it
if spaceRegex.search(text):
    text = spaceRegex.sub(' ', text)
# copy to clipboard
    print("Excess space(s) removed. Copied the new text to the clipboard.")
    pyperclip.copy(text)
else:
    print("No excess space found")

