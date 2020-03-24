import pyperclip, re, sys

# copy the text from the clipboard
text = str(pyperclip.paste())

# create 2 regexes for phone and email
phoneRegex = re.compile(
    r"""(
        (\d{3}|\(\d{3}\))?              # one or no area code
        (\s|-|\.)?                      # separator
        (\d{3})                         # first 3 digits
        (\s|-|\.)                       # separator
        (\d{4})                         # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extention if there is
        )""",
    re.VERBOSE,
)

emailRegex = re.compile(
    r"""(
    ([a-zA-Z0-9_.+-]+)                  # username
    @                                   # @ symbol
    ([a-zA-Z0-9+.]+)                    #domain nam
    \.                                  #dot
    ([a-zA-z]{2,5})                     #.com ,net etc
    )""",
    re.VERBOSE,
)

# Find all phone numbers and email addresses in the text
phoneNumbers = phoneRegex.findall(text)
emails = emailRegex.findall(text)
# paste them to the clipboard

if phoneNumbers and emails == None:
    print("No phone number or email address found")
    sys.exit()

matches = []
for groups in phoneNumbers:
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phoneNum += " x" + groups[8]
    matches.append(phoneNum)

for groups in emails:
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard")
    print("\n".join(matches))
else:
    print("No phone numbers or email address found.")
