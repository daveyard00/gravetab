# gravetab
Old experimental python program written for university course for writing guitar tablature

# Requirements
python 3.8.5+
sounddevice
numpy
piych
scipy
re
math

#about
this application is an experimental guitar tablature editor and is comprised of three main files,
- pytab_launcher.py
- gravetab.py
- tab_program.py

pytab_launcher is what the user should use to launch the other parts of the program, this was initially done
in order to keep everything seperate and 'tidy'.

gravetab is the experimental tablature tool that uses realtime pitch analysis to aim to tab music

tab_program is a text based tablature editor and the more usable of the tabbing tools.

#to-do
I may revisit this project in the future as I still feel that even after all this time, this is still a tool with a
lot of potential although a rewrite in another language such as Java or C++ may be the best course of action
- merge all parts of program in to one file
- rewrite text based interface using python-tcod
- less reliance on text files unless they're being stored in a temp folder such as AppData and generated on program launch
- convert pitch to midi note information including pitch and timing
- GuitarPro file export
