#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

'''
example: the clipboard has the following copied to it.

Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars

after running the program the out put should look like the following
after pasting:

* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars

'''

import pyperclip

text = pyperclip.paste()

#Seperate lines and add stars.
lines = text.split('\n')

for i in range(len(lines)): # loop through all indexes in the 'lines' list
    lines[i] = '* ' + lines[i] # add a star to each string in 'lines' list

text = '\n'.join(lines)

pyperclip.copy(text)

