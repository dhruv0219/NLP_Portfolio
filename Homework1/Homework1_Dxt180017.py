#Homework 1
#Dhruv Thoutireddy

#imports that are later used in the code
import sys
import pathlib
import re
import pickle

#creation of person class that contains last name, first name, middle initial, ID, and phone
class Person:
    def __init__(self, lastN, firstN, mid_initial, ID, phone):
        self.lastN = lastN
        self.firstN = firstN
        self. mid_initial = mid_initial
        self.ID = ID
        self.phone = phone

#getter function that gets the ID for key in dictionary
    def getID(self):
        return self.ID

#Display function that prints out the values of the specfic Person
    def display(self):
        print('Employee ID: ', self.ID)
        print('\t', self.firstN + ' ' + self.mid_initial + ' ' + self.lastN)
        print('\t', self.phone)

#function process_lines processes the text by cleaning up the values and making it more readable to the user
def process_lines(text):
    #splits the values by comma in the list
    new_text = []
    for emp in text:
        emp = emp.split(",")
        new_text.append(emp)

    length = len(new_text)

#converts all the first names, last names, and middle initials to uppercase
    for i in range(0,length):
        for j in range(0,2):
            new_text[i][j] = new_text[i][j].upper()

#makes sure that if there is no middle initial then set it equal to X
    for i in range(0,length):
        if new_text[i][2] == '':
            new_text[i][2] = 'X'

#Checks to see if ID is valid by checking to see if the first 2 values are Uppercase letters and the last 4 are digits
#if ID is incorrect user can enter the proper ID
    for i in range(0,length):
        ID_check1 = re.findall('[A-Z]', new_text[i][3])
        if len(ID_check1) != 2:
            print("\nID is invalid:" + new_text[i][3])
            print("ID is two uppercase letters followed by four digits")
            new_ID = input("please enter a valid ID: ")
            new_text[i][3] = new_ID
        ID_check2 = re.findall('[0-9]', new_text[i][3])
        if len(ID_check2) != 4:
            print("\nID is invalid:" + new_text[i][3])
            print("ID is two uppercase letters followed by four digits")
            new_ID = input("please enter a valid ID: ")
            new_text[i][3] = new_ID

#checks to see if the phone number is in the proper format
#if the phone number is not in the proper format user can enter the proper phone number
    for i in range(0,length):
        phone_length = len(new_text[i][4])
        if phone_length != 10:
            print("\nPhone number " + new_text[i][4] + " is invalid")
            print("Enter phone number in form of 123-456-7890")
            new_Phone = input("Enter phone number: ")
            new_text[i][4] = new_Phone
        else:
            dash = re.findall('(-)', new_text[i][4])
            if len(dash) != 2:
                print("\nPhone number " + new_text[i][4] + " is invalid")
                print("Enter phone number in form of 123-456-7890")
                new_Phone = input("Enter phone number: ")
                new_text[i][4] = new_Phone

#checks to see if the dashes are in the right spot for the phone number
    for i in range(0, length):
        m = new_text[i][4].find('-')
        n = new_text[i][4].rfind('-')
        if m != 3 and n != 7:
            print("\nPhone number " + new_text[i][4] + " is invalid")
            print("Enter phone number in form of 123-456-7890")
            new_Phone = input("Enter phone number: ")
            new_text[i][4] = new_Phone

#returns the value of dictionary with ID as the key value
    dict ={}
    for i in range(0,length):
        people = Person(new_text[i][0], new_text[i][1], new_text[i][2], new_text[i][3], new_text[i][4])
        dict[people.getID()] = people

    return dict

#main function that runs the program
if __name__ == '__main__':
    if len(sys.argv) < 2: #if arguments in control line are not the python file and csv, program will quit
        print('Please enter a file')
        quit()

#opens the csv file using the path given and reads it in
    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
        text_in = f.read().splitlines()

#saves the values as a dictionary from the process_lines function
    People = process_lines(text_in[1:])

#dictionary is written to pickle and then read pickle right after
    pickle.dump(People, open('people.pickle', 'wb'))
    People_input = pickle.load(open('people.pickle', 'rb'))

#prints values of the people
    print('\n\n' + 'Employee List:')

    for i in People_input.keys():
        People_input[i].display()

