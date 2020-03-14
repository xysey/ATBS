message = ""

countDict = {}

#count all the characters and add them to the count dictionary
#character as the key and the count as the value
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

#print all the characters and their count in a nice way
for character, count in countDict.items():
    print(character + ' - ' + str(count))