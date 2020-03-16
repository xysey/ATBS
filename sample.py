birthdays = {'Kenneth': 'August 29', 'Josel': 'August 8', 'Eugene' : 'April 8' }

while True:
    print('Enter a name: (blank to quit)')
    name = input()

    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I don't have birthday information for " + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print('Birthday database is updated')