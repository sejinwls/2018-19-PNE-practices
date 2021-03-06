import json
import termcolor

# -- Open the json file
f = open("person.json", 'r')

# Read the data from the file
# Now person is a dictionary with all the information
person = json.load(f)

# Print the number of people in the database
list_people = person["people"]
print("Total people in the database: {}".format(len(list_people)))
# Print the information of each person
for i, num in enumerate(list_people):
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person["people"][i]['Firstname'], person["people"][i]['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(person["people"][i]['age'])
    # Get the phoneNumber list
    phoneNumbers = person["people"][i]['phoneNumber']
    
    # Print the number of elements int the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])
