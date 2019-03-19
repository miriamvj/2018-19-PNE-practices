import json
import termcolor

f = open('person.json', 'r')

person = json.load(f)

print()

termcolor.cprint("Name:", 'green', end='')
print(person['First name'], person['Last name'])
termcolor.cprint("Age:", 'blue', end='')
print(person['Age'])

for i,num in person['Phone number']:
    termcolor.cprint("Phone {}".format(i), end='')
    termcolor.cprint("Type:", 'red', end='')
    print(num['type'])
    termcolor.cprint("Number:", 'red', end='')
    print(num['number'])

