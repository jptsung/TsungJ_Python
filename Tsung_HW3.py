#Question 1: Define a procedure histogram () that takes a list of integers
#and prints a histogram to the screen
#EX: histogram([4, 9, 7])

"""Prints a histogram using a for loop, checking the numbers over and over and printing out using an asterik"""
## docstrings need to be inside the function for help to work properly - see my example in histogram
def histogram (list): #defines a histogram
    """
    Prints a histogram using a for loop, checking the numbers over and over and printing out using an asterik
    """
    for n in range(0, len(list)): #for the number in the range from 0
        print ('*' * list[n]) #prints out the * multiplied by the number n
    return (list) #returns the list of numbers used

#histogram([4,9,7]) #prints histogram

#Question 2: Write a function max_in_list() that takes a list of numbers and returns the largest one

"""Uses a for and while loop to loop through the values and replace the maximum value with the next value if it's greater"""

def max_in_list(list): #defines the function max_in_list
    max = list[0] #initializes the first number as the max
    for n in list: #for the number in the list
        while n > max: #if or while the number n is greater or equal to max
            max = n #loops through and replaces max into a new value if n is greater than max
    return max #returns largest value

#max_in_list([55,342,3,1])

#Question 3: Write function that maps a list of words into a list of integers representing lengths of words

"""Function maps a list of words into a list of integers representing lengths of words"""

def words(list):
    integer = [] #initializes the integer to a blank zero
    for string in list:
        integer.append(len(string)) #append function to add integers in the string of letters
    return (integer) #returns the integer that coincides with the number of letters in the word

# words(['Georgetown','University','Hoya', 'Saxa'])

#Question 4: Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

"""Function finds the longest word of a list of words and returns the length of that word using previous code"""

def find_longest_word(list): #defines a function that finds the longest word
    return max_in_list(words(list)) #returns by looping the Q3 function which found the integers representing word length
                                    #loops within the max_in_list function to find the greatest number among the list produced
# find_longest_word(['Georgetown','University','Hoya', 'Saxa'])
    

#Question 5: Write a function filter_long_words() that takes a list of words and an integer n

"""Function returns the list of words that are longer than n"""

## Should only return words longer than n
def filter_long_words(wordlist, n): #defines the function
    listofwords = []
    for words in wordlist: #for loop generates length of words and compares to n
        if len(words) >= n:listofwords.append(words) #selects words with length greater than n
    return (listofwords)
# filter_long_words (['Georgetown','University','Hoya', 'Saxa'],5)

#Question 6: Write a version of a palindrome recognizer

"""Function accepts phrase palindromes where punctuation, capitalization, spacing is ignored"""

def palindrome(phrase): #defines function palindrome for a phrase       
    
    i=[n for n in phrase.lower() if n.isalpha()] #initialize 'i' to ignore capitalization, punctuation, and spacing
    reverse=i[::-1] #reverses a string by [begin:end:step]; skips begin and end, and defines step as -1 to reverse
    
    while i==reverse:  #tests while initial phrase read forward is equalivalent to phrase read backwards
        return (True) #returns 'True' if the word is the same as it is reversed
    else: #otherwise, if it is not a palindrome
        return (False) #returns 'False' because word is not a palindrome
# palindrome("Lisa Bonet ate no basil")

#Question 7: A pangram is a sentence that contains all the letters of the English alphabet at least once...

"""Write a function to check a sentence to see if it is a panagram or not"""

import re #imports the regular expression operation

def pangram(sentence):
    letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz" #listing all letters upper and lowercased
    count = 0 # initialize count to 0
    string = "" #initalizes string
    
    if len(sentence) < 26: #if the sentence is below 26 characters, then it can't include every letter of the alpahabet
        return (False) #returns false because doesn't include all letters of alphabet
    else:
        sentence = re.sub('^[a-zA-Z]','',sentence) #putting carat outside of bracket so any a-z or A-Z at the start of a line         
        for n in range(len(letters)): #given that the range 
            if letters[n] in sentence: 
                count += 1 #then add all the letters to the count
        while count == 26: #when the count includes the 26 letters
            return True #then return True
        else:
            return False #returns False if not a pangram
        
# pangram ("The quick brown fox jumps over the lazy dog")

#Question 8: write a Python program capable of generating all the verses of the song

"""Function generates all the verses of the song through substitution"""

def verses(n): #defines the function of n as a number
 
    for x in range(n,0,-1): #loops the string x throughout the verse and subtracting by one at the end
        print(str(x)+" bottles of Coke on the wall, "+ str(x) +" bottles of Coke.") 
        print("Take one down, pass it around, "+ str(x-1) +" bottles of Coke on the wall.")
        print (" ") #prints a space between each verse
         
# verses(99) #verse starts at 99 bottles

#Question 9: Represent a small bilingual lexicon as a Python dictionary

"""Function translate() takes list of English words and returns a list of Swedish words"""

def translate(list):
    dictionary = {"merry":"god", #assigns the dictionary of English words to Swedish words
                  "christmas":"jul",
                  "and":"och",
                  "happy":"gott",
                  "new":"nytt",
                  "year":"år"}
    translation = [] #initiatlize the translated result to blank zero

    for word in list: 
        while word not in dictionary: #word is not in the mini dictionary
            print ("Cannot be translated") #can't print a translation so print this statement instead
        else: # if word is in dictionary
            translation.append(dictionary[word]) #using the append function to append a passed word into the existing list
    return translation

# translate(["merry", "christmas", "and", "happy", "new", "year"]) #testing the sentence

#Question 10: Write a function char_freq() that takes a string and builds a frequency listing of characters 

"""Function represents frequency as a Python dictionary; builds a frequency listing by taking a string"""

def char_freq(string):
    character = "" #initialize character
    dictionary = {i: 0 for i in string} #initialize dictionary frequency to 0 in the string
    
    for n in string: dictionary[n] = dictionary[n] + 1 #for every n character in the string, count total appearances
    return (dictionary) #returns the dictionary frequency

# char_freq("abbabcbdbabdbdbabababcbcbab")

#Question 11: Caesar Cipher

"""Function will implement an encoder/decoder of ROT-13"""

def cipher(string): #defines the function cipher
    list = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
            'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
            'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
            'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
            'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
            'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
            'W':'J', 'X':'K', 'Y':'L', 'Z':'M'} #lists the dictionary and translated characters
    translation = '' #initiate translation to blank zero
    keys = list.keys() #initiate keys to retrieve the keys as a list all at once
    for i in string: #for loop with the characters in string
        if i in keys:translation = translation + list[i] #replace dictionary values
        else:
            translation = translation + i #if not in list, then add character without the change
    return translation

# cipher("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")

#Question 12: Define a simple "spelling correction" function correct() that takes a string

""" Function correct() will take string and see that two+ spaces are compressed to one; inserts extra space after ."""

import re #imports the re module which includes regular expression patterns

def correct(string): #defines function correct()
    string = re.sub(' +', ' ', string) #two or more occurrences of the space character is compressed into one
    string = re.sub(r'\.([^ ])', r'. \1', string) #inserts an extra space after a period if the period is followed by letter
    return (string) #returns the corrected string 

# correct("This       is very funny and  cool.Indeed!")

#Question 13: Define a function make_3sg_form() which returns third person singular form

"""Function makes verb in infinitive form return as third person singular form"""

import re 

def make_3sg_form(verb): #defines function
    while verb.endswith('y'): #while verb ends with a 'y', then...
        return re.sub('y$', 'ies', verb) #substitutes the verb ending in 'y' for an 'ies'
    i = ('ch', 'o', 's', 'sh', 'x', 'z') 
    while verb.endswith(i): #assuming verb ends in the above list of endings
        return re.sub('$', 'es', verb) #replaces them with 'es'
    else:
        return re.sub('$', 's', verb) #all other endings end with an 's'

# make_3sg_form("brush")

#Question 14: Define a function make_ing_form() 

"""Function that, given a verb in infinitive form, returns it in present participle form""" 

#If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
#If the verb ends in ie, change ie to y and add ing
#For words consisting of consonant-vowel-consonant, double the final letter before adding ing
#By default just add ing

import re
## This doesn't work in all cases, see my test cases below - Prof G
def make_ing_form(verb): 
    while verb.endswith("e") and (verb[-2].endswith("e") or len(verb) == 2): #for verb exceptions
        return verb + "ing"  #don't drop anything, just add "ing"
    while verb.endswith("e"): #if just normal "e"
        return verb[:-1] + "ing" #drop last character and replace with "ing"
    while verb.endswith("ie"): #verbs ending with "ie" 
        return verb[:-2] + "ying" #return by depleting last two characters and placing on "ying"
    while re.search("[^aieou][aieuo][^aieou]$", verb): #words consisting of consonant, vowel, consnant
        return re.sub("(.)$", r"\1\1ing", verb) #doubles final letter before adding ing, using substitution command
    else: #otherwise, if just a consonant
        return re.sub("$", "ing", verb) #returns verb with "ing" if just default"

# make_ing_form("dream")

##Test Cases
help(histogram)
help(make_ing_form)

print("1 Histogram ", histogram([1,2,3,5,6,7,6,5,4,3,2,1]), '\n')

print("2 Max in List 77 ", max_in_list([1,2,3,77,4,5,6,7]), '\n')

print("3 word to length map 3,5,7,4 ", words(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("4 Longest word 7 ", find_longest_word(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("5 filter long words snake, dolphin ", filter_long_words(['dog', 'snake', 'dolphin', 'cats'],4), '\n')

print("6 Palindrome phrase TRUE ", palindrome("Go hang a salami I'm a lasagna hog."), '\n')

print("7 Pangram TRUE ", pangram("The quick brown fox jumps over the lazy dog."), '\n')

print("8 Cokes \n", verses(9))

print("9 Translating to Swedish ['god', 'jul', 'gott'] ", translate(['merry', 'christmas', 'happy']), '\n')

print("10 Char Freq {'a': 7, 'c': 3, 'b': 14, 'e': 2, 'd': 3, 'g': 7, 'f': 3} ", char_freq("agbbabgcbdbabdgbdbabageebabcbgcbffgfabg"), '\n')

print("11 Decoder Caesar cipher? I much prefer Caesar salad!", cipher("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"), '\n')

print("12 correct This is very funny and cool. Indeed!", correct("This is very funny and cool.Indeed!"), '\n')

print("13 3ps brushes ", make_3sg_form("brush"), '\n')
print("13 3ps tries ", make_3sg_form("try"), '\n')
print("13 3ps runs ", make_3sg_form("run"), '\n')
print("13 3ps fixes ", make_3sg_form("fix"), '\n')

print("14 ing lying ", make_ing_form("lie"), '\n')
print("14 ing seeing ", make_ing_form("see"), '\n')
print("14 ing moving ", make_ing_form("move"), '\n')
print("14 ing hugging ", make_ing_form("hug"), '\n')