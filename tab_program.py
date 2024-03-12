import numpy as np
import os
riff_number = 1
global position
blank_tab = open('blank_tab.txt','r')
blank_tab = blank_tab.read()
blank_tab = blank_tab.split('\n')
string_arr = ["e","B","G","D","A","E"]
chord_mode = False
#low_e = "-------------------------"
strings_placed = []
positions_placed = []


def system_message(message):
    os.system('cls')
    print(message)

def split_all_chars(word):
    return list(word)

#def clear_tab():
#    strings = []
#    for i in blank_tab:
#        strings = np.array(strings)
#        strings = np.append(strings, split_all_chars(i))
#       joined_str = ""
#       for i in strings:
#           joined_str = "".join(i)
#           print(joined_str)
#  print(strings)
        

def store_note(string_val, position):
    strings_placed.append(string_val)
    positions_placed.append(position)



strings = []
for i in blank_tab:
    strings.append(split_all_chars(i))

strings = np.array(strings)

class note:
    def __init__(self, string, pos, fret):
        self.string = string
        self.pos = pos
        self.fret = fret
        np.put(strings[string], pos, fret)

        

print("enter name of project")
project_name = input()
position = 0
exit_loop = False
print("available instructions, help, chord, hammer on, pull off, slide, undo, place notes by specifying a string (E,A,D,G,B,e) or '-' to go forward")
while exit_loop == False:
    for i in strings:
        joined_str = "".join(i)
        print(joined_str)
    loop_choice = input("enter an instruction or string (E,A,D,G,B,e)")
    if loop_choice == "help":
        print("this will open a help text file eventually")
    elif loop_choice in string_arr:
        print(string_arr.index(loop_choice))
        string_val = string_arr.index(loop_choice)
        print("user entered string")
        fret = input("what fret?")
        note(string_val, position, fret)
        store_note(string_val, position)
        if chord_mode == True:
            os.system('cls')
            print('please enter the next string you will place a note on')
        else:
            position += 2
            os.system('cls')
    elif loop_choice == "undo":
        position -= 2
        note(string_val, position, '-')
        #os.system('cls')
        system_message('removed last note')
    elif loop_choice == "chord":
        if chord_mode == True:
            chord_mode = False
            #os.system('cls')
            system_message('chord mode disabled')
            position += 2
        elif chord_mode == False:
            chord_mode = True
            os.system('cls')
            print('chord mode enabled, posistion will not update after placing a new note')
    elif loop_choice == "-":
        position += 2
        system_message("advanced to position %s"%position)
    elif loop_choice == "save":
        print("writing riff to %s"%project_name)
        file = open(project_name+".txt","a")
        file.write("riff %s"%riff_number+"\n")
        for i in strings:
            joined_str = "".join(i)
            file.write(joined_str+"\n")
        file.close()
        #clear_tab()
        counter = 0
        riff_number += 1
        for i in positions_placed:
            note(strings_placed[counter], i, "-")
            counter += 1
        counter = 0
        position = 0
        
        strings_placed = []
        positions_placed = []
        system_message("saved work")
        


            
