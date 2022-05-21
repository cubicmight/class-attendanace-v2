from consolemenu import *
from consolemenu.items import *

import os
import pickle
import time

OUTPUT_FILE_PICKLE = 'output_file.pickle'

dictx = {'monday': {},
         "tuesday": {},
         "wednesday": {},
         "thursday": {},
         "friday": {}}


def print_dictionary():
    global dictx
    for key in dictx:
        print(key, '->')
        key_2 = dictx[key]
        for key_3 in key_2:
            print("\t%s was %s" % (key_3, key_2[key_3]))


def view_attendance():
    global dictx
    print_dictionary()
    save_file(dictx)
    time.sleep(5)


def add_student_names():
    global dictx
    input_name = input("\nPlease input a name (The word status will be replaced with the student's status when you "
                       "take attendance) : \n")
    dictx['monday'][input_name.upper()] = "Status"
    dictx['tuesday'][input_name.upper()] = "Status"
    dictx['wednesday'][input_name.upper()] = "Status"
    dictx['thursday'][input_name.upper()] = "Status"
    dictx['friday'][input_name.upper()] = "Status"
    print("Your class is: ")
    print_dictionary()
    time.sleep(5)
    print("\n")


def take_attendance():
    global dictx
    existing_name = input("\nPlease input an existing name to take attendance for: \n")
    if existing_name.upper() in dictx['monday'].keys():
        y = input("\nPlease type the day that you would like to take attendance for (EX: Monday):\n ").upper()
        s = input("\nPlease type P if they are present, A for absent, and T for tardy: ")
        if y == 'MONDAY':
            dictx['monday'][existing_name.upper()] = s.upper()
        elif y == 'TUESDAY':
            dictx['tuesday'][existing_name.upper()] = s.upper()
        elif y == 'WEDNESDAY':
            dictx['wednesday'][existing_name.upper()] = s.upper()
        elif y == 'THURSDAY':
            dictx['thursday'][existing_name.upper()] = s.upper()
        elif y == 'FRIDAY':
            dictx['friday'][existing_name.upper()] = s.upper()
        else:
            print("Please type a valid day.")
            take_attendance()
        print("\nThe weeks attendance is as follows: ")
        print_dictionary()
        time.sleep(5)
        print("\n")
    else:
        print("That student is not in the system. \n")
        time.sleep(5)

def delete_all():
    global dictx
    dictx['monday'] = {}
    dictx['tuesday'] = {}
    dictx['wednesday'] = {}
    dictx['thursday'] = {}
    dictx['friday'] = {}


def change_name():
    global dictx
    existing_name = input("\nPlease input a name to CHANGE the name of: \n")
    name_upper = existing_name.upper()
    if name_upper in dictx['monday'].keys():
        new_name = input("Input a new name for " + existing_name + ":\n").upper()
        m1 = dictx['monday'][name_upper]
        t1 = dictx['tuesday'][name_upper]
        w1 = dictx['wednesday'][name_upper]
        th1 = dictx['thursday'][name_upper]
        fr1 = dictx['friday'][name_upper]

        del dictx['monday'][name_upper]
        del dictx['tuesday'][name_upper]
        del dictx['wednesday'][name_upper]
        del dictx['thursday'][name_upper]
        del dictx['friday'][name_upper]

        dictx['monday'][new_name] = m1
        dictx['tuesday'][new_name] = t1
        dictx['wednesday'][new_name] = w1
        dictx['thursday'][new_name] = th1
        dictx['friday'][new_name] = fr1
        save_file(dictx)
        print_dictionary()
        print("\nThe Name has been edited and changed. \n")
        time.sleep(5)
    else:
        print("\nThere is no student with that name in your attendance. \n")
        time.sleep(5)


def save_file(save_dictx):
    with open(OUTPUT_FILE_PICKLE, "wb") as outfile:
        pickle.dump(save_dictx, outfile)


def delete_name():
    global dictx
    del_name = input("\nPlease input a name to DELETE here: ")
    if del_name.upper() in dictx['monday'].keys():
        dictx['monday'].pop(del_name.upper())
        dictx['tuesday'].pop(del_name.upper())
        dictx['wednesday'].pop(del_name.upper())
        dictx['thursday'].pop(del_name.upper())
        dictx['friday'].pop(del_name.upper())
        print("\nThe inputted Name and it's information has been deleted.")
        y = int(input("\nWould you like to delete everyone in your class? Type 1 for yes and 2 for no: \n"))
        if y == 1:
            z = int(input("\nAre you sure that you would like to delete all names? Type 1 for yes and 2 for no: "))
            if z == 1:
                delete_all()
                print("\nYour attendance roster has been cleared.\n")
                time.sleep(5)
                print_dictionary()
                save_file(dictx)
            else:
                save_file(dictx)
        else:
            return
    else:
        print("\nThere is no one in your attendance with that name. \n")
        save_file(dictx)


def main_menu_display():
    global dictx
    menu = ConsoleMenu("Class Attendance", "Weekly")
    one = FunctionItem("Type 1 to view attendance", view_attendance)
    two = FunctionItem("Type 2 to add a student to your attendance.", add_student_names)
    three = FunctionItem("Type 3 to change a student's name.", change_name)
    four = FunctionItem("Type 4 to delete a name.", delete_name)
    five = FunctionItem("Type 5 to take attendance.", take_attendance)
    six = MenuItem("MADE FOR HIGH TECH HACKS 2022")
    menu.append_item(one)
    menu.append_item(two)
    menu.append_item(three)
    menu.append_item(four)
    menu.append_item(five)
  menu.append_item(six)
    menu.show()
save_file(dictx)


def load_file():
    global dictx
    if os.path.exists(OUTPUT_FILE_PICKLE):
        try:
            with open(OUTPUT_FILE_PICKLE, "rb") as uu:
                dictx = pickle.load(uu)
        except IOError:
            print("\nSomething went wrong saving the file. \n")


if __name__ == "__main__":
    load_file()
    while True:
        return_val = main_menu_display()
        if not return_val:
            break
