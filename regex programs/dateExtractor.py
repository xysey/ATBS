#! python3
# a program to extract and format dates within a text and copy it to clipboard
import re, pyperclip

matches = []
# paste the text from the clipboard
text = str(pyperclip.paste())

dateRegexNormal = re.compile(
    r"(0?[1-9]|1[012])[ /-](0?[1-9]|1[0-9]|2[0-9]|3[01])[ /-](\d{4})"
)

dateRegexYearFirst = re.compile(
    r"(\d{4})[ /-](0?[1-9]|1[012])[ /-](0?[1-9]|1[0-9]|2[0-9]|3[01])"
)
# search for dates
# format the dates
for groups in dateRegexNormal.findall(text):
    month, day = "", ""
    if len(groups[0]) < 2:
        month = "0" + groups[0]
    else:
        month = groups[0]
    if len(groups[1]) == 1:
        day = "0" + groups[1]
    else:
        day = groups[1]
    matches.append("/".join([month, day, groups[2]]))

for groups in dateRegexYearFirst.findall(text):
    month, day = "", ""
    if len(groups[1]) == 1:
        month = "0" + groups[1]
    else:
        month = groups[1]
    if len(groups[2]) == 1:
        day = "0" + groups[2]
    else:
        day = groups[2]
    matches.append("/".join([month, day, groups[0]]))
# copy the dates to the clipboard
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard")
    print("\n".join(matches))
else:
    print("No date found.")
