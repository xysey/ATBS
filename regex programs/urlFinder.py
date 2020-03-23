#! python3
# a program that finds url

import re, pyperclip

text = str(pyperclip.paste())



urlRegex = re.compile(r'(https?://(www\.)?([a-zA-Z0-9_-]+)\.([a-zA-Z\./0-9]+))')

urls = urlRegex.findall(text)

if len(urls) > 0:
    print('Url/s found')
    for url in urls:
        print(url[0])
else:
    print('No url/s found')
