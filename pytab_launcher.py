import time
import os
print('''
_|_|_|              _|_|_|_|_|          _|        
_|    _|  _|    _|      _|      _|_|_|  _|_|_|    
_|_|_|    _|    _|      _|    _|    _|  _|    _|  
_|        _|    _|      _|    _|    _|  _|    _|  
_|          _|_|_|      _|      _|_|_|  _|_|_|    
                _|                                
            _|_|     
''')
print("""welcome to PyTab, a guitar tablature creation tool
there's two ways to input, one is a basic text editor and the other is a
VERY EXPERIMENTAL audio input, what do you want, text or audio?""")
choice = input()
if choice == "text":
    print("wise choice, opening the text based tab editor")
    time.sleep(3)
    os.system("tab_program.py")
elif choice == "audio":
    print("""when the next window opens up, after you enter your project name,
you will have 15 seconds (roughly) to record a riff, this will be written to a file entitled [project name].txt,
at which point you will return here and then you can specify audio again and record a new riff. press enter to confirm""")
    input()
    print("ok, sending you to the audio input window, have fun!")
    time.sleep(3)
    os.system("audio_input.py")
    
