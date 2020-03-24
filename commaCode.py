def commaCode(listahan):
    stringList = ""
    for item in listahan:
        if listahan.index(item) == (len(listahan) - 1):
            if type(item) != type("a"):
                item = str(item)
            stringList = stringList + "and " + item
            break
        if type(item) != type("a"):
            item = str(item)
        stringList = stringList + item + ", "

    return stringList


spam = ["apples", "bananas", "tofu", "cats", 1, 12.3]
print(commaCode(spam))
