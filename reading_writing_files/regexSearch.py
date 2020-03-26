#! python3
"""
a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.
"""
import os, re

print("Whats is the path of the folder?")
path = r"{}".format(input())
print("What is the regex pattern?")
pattern = r"{}".format(input())
# remember if you don't want to join the dirname and filename use chdir
# if you don't want to then join them in that open method os.path.join(path, file)
os.chdir(path)
files = os.listdir(path)

lines = []
for file in files:
    if file[-4:] == ".txt":
        textFile = open(file)  # <---- join them here
        text = textFile.read()
        textFile.close()
        linya = re.finditer(r"{}".format(pattern), text)
        for match in linya:
            lines.append(match.group())
print(lines)
