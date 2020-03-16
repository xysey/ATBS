import pprint

message = '''
If you import the pprint module into your programs, you’ll have access to
the pprint() and pformat() functions that will “pretty print” a dictionary’s
values. This is helpful when you want a cleaner display of the items in a
dictionary than what print() provides. Modify the previous characterCount.py
program and save it as prettyCharacterCount.py.
'''

countDict = {}

#count all the characters and add them to the count dictionary
#character as the key and the count as the value
for character in message:
    countDict.setdefault(character, 0)
    countDict[character] = countDict[character] + 1

# print all the characters and their count in a nice way
# for character, count in countDict.items():
#     print(character + ' - ' + str(count))

# pprint.pprint(countDict)
print(pprint.pformat(countDict))