#! python3

# Paste text from the clipboard
import pyperclip

text = pyperclip.paste()

# Do something about it
text = text.split("\n")
for i in range(len(text)):
    text[i] = "* " + text[i]

# Copy the text to the clipboard
pyperclip.copy("\n".join(text))
