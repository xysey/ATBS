#! python3
"""
A  program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file.
"""
import re

# open a text file
textFile = open(".\\sample.txt")
text = textFile.read()
textFile.close()
# search for the KEYWORDS in the text
adjRegex = re.compile(r"ADJECTIVE")
nRegex = re.compile(r"NOUN")
advRegex = re.compile(r"ADVERB")
vRegex = re.compile(r"VERB")
# substitute the KEYWORDS with users input
boolKeywords = {
    "adjective": adjRegex,
    "noun": nRegex,
    "adverb": advRegex,
    "verb": vRegex,
}

for word, regex in boolKeywords.items():
    if regex.search(text) is not None:
        print("Enter a " + word)
        w = input()
        text = regex.sub(w, text)
# save the new text to a text file and print it.
madlibs = open("madlibs.txt", "w")
madlibs.write(text)
madlibs.close()
print(text)
