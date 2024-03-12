#gravetab

#while true loop
#see if a key is pressed and apply tab modifier
#take input from audio input
#get frequency
#convert to note
#convert to tablature position
#see which position is logical
#add to tab array
#output as txt when needed

#get volume of input
#if volume greater than (whatever)
#record sample
#check pitch of sample

#used as a base
#https://stackoverflow.com/questions/40138031/how-to-read-realtime-microphone-audio-volume-in-python-and-ffmpeg-or-similar
#https://realpython.com/playing-and-recording-sound-python/#python-sounddevice_1
#https://dzone.com/articles/musical-pitch-notation

import sounddevice as sd
import numpy as np
import pitch
from scipy.io.wavfile import write
import re
from math import log2, pow, log

global position
a4=440
c0=a4*pow(2,-4.75)
name = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
fs = 44100
seconds = 0.2
mod_string = ""
tab_contents = []
blank_tab = open('blank_tab.txt','r')
blank_tab = blank_tab.read()
blank_tab = blank_tab.split('\n')
strings = []
position = 1


def split_all_chars(word):
    return list(word)


for i in blank_tab:
    strings.append(split_all_chars(i))

strings = np.array(strings)



# -= STRING NOTATION =-
# 5 - high e
# 4 - b
# 3 - g
# 2 - d
# 1 - a
# 0 - e
# -= STRING NOTATION =-
class note:
    def __init__(self, string, pos, fret):
        self.string = string
        self.pos = pos
        self.fret = fret
        np.put(strings[string], pos, fret)


def note_pitch(freq):
    h = round(12*log2(freq/c0))
    octave = h // 12
    n = h % 12
    note = str(name[n])+str(octave)
    print(note)
    find_fret(freq)


def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    if volume_norm > 10:
        print("playing a sound")
        sample = sd.rec(int(seconds*fs), samplerate=fs, channels=1)
        sd.wait()
        write('sample.wav',fs,sample)
        p = pitch.find_pitch('sample.wav')
        note_pitch(p)

def remove(og_string):
    global mod_string #not best practice but return just isn't working
    pattern = '[0-9]'
    mod_string = re.sub(pattern, '', og_string)

def find_fret(freq): #takes in hz
    global position
    note_freqs = ["e2","a2","d3","g3","b3","e4"]
    freq = round(freq) #provides more leniancy with no real downside
    frequencies=[82,110,146,195,246,329]
    for i in range(len(frequencies)): #find what string it's probably played on
        try:
            if frequencies[i]<=freq<frequencies[i+1]:
                print("played on ",frequencies[i])
                string_index=i
                break
            else:
                print("not played on ",frequencies[i])
        except:
            print("played on high e probably")
            string_index=i
    #find how many semitones away it is using logs
    fret_played = log(frequencies[i]/freq)/log(pow(2,1/12))
    fret_played = abs(round(fret_played))
    print(position)
    note(abs(5-string_index),position,fret_played)
    position += 2
        
        #calculate distance from open string to note
        #check if it's the right octave, if not add 12 frets
        #use lowest number value or closest to previously placed note
        #copy string txt replace %s

     
with sd.Stream(callback=print_sound):
    sd.sleep(10000)


for i in strings:
    joined_str = "".join(i)
    print(joined_str)


