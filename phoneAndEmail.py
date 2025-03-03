'''
Project: Phone Number and Email Address Extractor

Should be able to copy a bunch of text to the clipboard and make it paste all the 
U.S phone numbers & email addresses found within the text.

1. Get the text off the clipboard.
2. Find all U.S. phone numbers and email addresses in the text.
3. Paste them onto the clipboard.

'''

#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import re, pyperclip

# regular expression that looks for a phone number
phoneNum = re.compile(r'''(
                      (\d{3}|\(\d{3}\))? # looks for area code 
                      (\s|-|\.)? # seperators
                      (\d{3}) # first 3 digits
                      (\s|-|\.) # seperator
                      (\d{4}) #last 4 digits
                      (\s*(ext|x|ext.|)\s*(\d{2,5}))? # looks for an extention
                      )''', re.VERBOSE)

# regular expression that looks for an email addresss
emailAddress = re.compile(r'''(
                          ([a-zA-Z0-9._%+-]+)
                          @
                          ([a-zA-Z0-9._%+-]+)
                          (\.[a-zA-Z]{2,4})
                          )''', re.VERBOSE)


#TODO: Find matches in the clipboard text

text = str(pyperclip.paste())
match = []

for groups in phoneNum.findall(text):
    number = '-'.join([groups[1], groups[3], groups[5]])

    if groups[8] != '':
        number += ' x' + groups[8]
    
    match.append(number)

for groups in emailAddress.findall(text):
    match.append(groups[0])


#TODO: Copy results to the clipboard

if len(match) > 0:
    pyperclip.copy('\n'.join(match))
    print('Copied to clipboard:')
    print('\n'.join(match))
else:
    print('No phone numbers or email addresses found.')
          








