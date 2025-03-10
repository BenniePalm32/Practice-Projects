# A program that translates English into Pig Latin


print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a','e','i','o','y')

pigLatin = [] # A list of the words in Pig Latin

for word in message.split():

    # Seperate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha:
        prefixNonLetters += word[0]
        word = word[1:]
    
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Seperate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters = word[-1] + suffixNonLetters
        word = word[:-1]

    # Remember if the word was in wuppercase or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Make the word lowercase for translation

    # Separate the consonants at the strat of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to the uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(' '.join(pigLatin))
          

