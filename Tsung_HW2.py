#Question 1: Define a 'fib' that takes a number, 'n', as a parameter and prints all the Fib numbers less than 'n'

## You need to add header documentation using doc strings.

def fib(n): #defines the fib function
    
    a,b = 0,1 #initializing a to 0 and b to 1 as the first two values in the sequence
    while a < n: #loops through until condition is met on the fib function where a is the fib num that is less than n
        print(a) #prints a 
        a, b = b, a+b #each subsequent number is the sum of the previous two
        #a(x) = a + b as the function
        #a(x) = a == b as b becomes a
        #b = x == a+b as b becomes equal to the function
    
fib(1000) #prints all the Fibonacci numbers less than 'n' = 1000 to the screen 

#Question 2: Define a function mymax() that takes two numbers as arguments and returns the largest of them. 
#Use the if-then-else construct

def mymax(a,b): #function that takes two numbers as arguments

    if a >= b: #if a is greater than or equal to b
        return (a) #then display a
    else: #otherwise,
        return (b) #you know b is greater, so return b
        
mymax(23,32) #when b is greater

#Question 3: Define a function max_of_three() that takes three numbers and returns the largest

def max_of_three (a,b,c): #compares a to b, a to c, and b to c
    
    while a >= b and a >= c: #if a is greater or equal to both b and c
        return (a) #then return value of 'a' because it is the greatest
    while b >= c and b >= a: #if b is greater or equal to both a and c
        return (b) #then return value of 'b' because it is the greatest
    else: #otherwise
        return (c) #return c
        
max_of_three(33,55,3) 

#Question 4: Define a function mylen() that computes length of a list or string

def mylen(string): #function takes string 
    
    length = 0 #set length to 0 unless otherwise
    for x in string: 
        length = length + 1 #adding 1 for every count
    return (length)

mylen('Georgetown')

#Question 5: Write a function that takes a character and returns 'True' if vowel, 'False' if otherwise

def vowel(alphabet): #defines the function

    ## This logic is not the best way to code this section.
    # while alphabet in "Yy": #Y and y are an exception
    #     return "Sometimes" #Y can sometimes be a vowel
    # Great you checked upper and lower case
    if alphabet in "AaEeIiOoUu": #if the alphabetical letter is a vowel
        return True #then return True
    else: #Otherwise
        return False #it will return False
    
# letter("G") #testing the function with the best letter

#Question 6: Write a function translate() that will translate a text into "rovarspraket"
#double every consonant and place an occurrence of "o" in between
#EX: "this is fun" returns the string "tothohisos isos fofunon"

## Blanks should be treated like vowels.

def translate(x): #defines the function translate()
    
    letter = "" #initialize letter as a blank
    for consonant in x:
        if consonant not in ("AaEeIiOoUu"): #consonant not a vowel (doesn't include Y or y)
            letter = letter + consonant + "o" + consonant #translates word to adding an o and the same consonant
        else:
            letter = letter + consonant #if vowel, then just continue with next consonant
    return (letter) #returns the letter(s), letter-by-letter
    
translate("Umbrella") #translating Umbrella to test out case-sensitivity in vowels

#Question 7, Part 1: Define a function sum() that sums all numbers in a list of numbers

def sum(numbers): #defining the additive function
    
    x = 0 #initialize
    for digits in numbers: x = x + digits #for the numbers in the function, x will add and then compute digits after each loop
    return x #x will then be returned

sum([1,2,3,4])  #testing the addition of the list of numbers of 1,2,3 and 4

#Question 7, Part 2: Define a function multiply() that multiplies all numbers in a list of numbers

def multiply (nums):
    
    mult = 1 #initialize mult
    for digits in nums: mult = mult * digits #for loop computes the multiple of one digit per loop
    return mult #returns the solution

multiply ([1,2,3,4]) #testing multiplication of the list of numbers 1-4

#Question 8: Define a function reverse() that computes the reversal of a string
#EX: reverse ("I am testing") to return "gnitset ma I"

def reverse (string):
   
    word = "" #initialize word
    for x in reversed(string): #for loop reverses the string for each letter
        word = word + x #places reversed word letters in order
    return word #returns the new word

reverse("I am testing")

#Question 9: Define a function is_palindrome() that recognizes words that look the same written backwards
#EX: radar is a palindrome; should return True

def is_palindrome(word): #this solution inspired from stackoverflow with the [begin:end:step]
    
    while word == word[::-1]: #reverses a string by [begin:end:step]; skips begin and end, and defines step as -1 to reverse
        return (True) #returns 'True' if the word is the same as it is reversed
    else: #otherwise, if it is not a palindrome
        return (False) #returns 'False' because word is not a palindrome
        
is_palindrome ("radar") #tests palindrome

#Question 10: Write a function is_member() that takes a value x and a list of values a;
#returns True if x is a member of a, False otherwise

def is_member(value_x,list_a): #defining the function 

    while value_x in list_a: #if x is a member of a
        return (True) #then return true
    else: #if x is not a member of a
        return (False) #returns False
    
is_member('G', 'Gerhard') #testing with letters and words

#Question 11: Define a function overlapping() that takes two lists 
#returns True if they have at least one member in common, False otherwise
#May use is_member() function or in operator but should write it using two nested for-loops

def overlapping(list_1, list_2): #defining the function
    
    for var1 in list_1: #var1 is a given member of list_1
        for var2 in list_2: #var2 as a given member of list_2
            while var2 == var1 or var1 == var2: #if the list_1 member and list_2 are equal and vice-versa, then..
                return (True) #return True because they have at least one member in common
            else: #otherwise
                return (False) #returns False if no commonality between lists

overlapping([1,3,5,7],[1,2,3,4,5]) #testing True

#Question 12: Define a function generate_n_chars() that takes an integer n and a character c and returns a string
#n characters long, consisting only of c:s
#EX: generate_n_chars(5,"x") returns string "xxxxx"

def generate_n_chars(n,c):
    
    string = '' #initialize an empty string
    for integer in range( 0, n ): string += c #equivalent to string = string + c
                                              #loops for an integer n within the range from 0 to n
    return (string) #returns the string of characters for the amount of integers

## This is a 'funny' test case - =D
generate_n_chars(10,"HA") #when you find something really funny, you laugh:

##TEST CASES

print('#1\n')
fib(500)
print('\n')

print('#2\n')
print(mymax(45,987), '\n')

print('#3\n')
print(max_of_three(3,4,5),'\n')

print('#4\n')
print(mylen('Gerhard'))
print(mylen([1,2,3,4,5,6,7]))
print('\n')

print('#5\n')
print(vowel('e'))
print(vowel('H'))
print('\n')

print('#6\n')
print(translate("this is fun"))
print(translate('aeiou'))
print(translate('YYYYYYY'))
print(translate("mmmmmm"))
print('\n')

print('#7\n')
print(sum([1,2,3,4,5]))
print('\n')

print('#8\n')
print(multiply([0,1,2,3]))
print(multiply([1,2,3,4]))
print('\n')

print('#9\n')
print(reverse("gnitset ma I"))
print('\n')

print('#10\n')
print(is_palindrome('radar'))
print(is_palindrome('Gerhard'))
print('\n')

print('#11\n')
print(is_member('dog', ['cat', 'dog', 'zebra']))
print(is_member(3, [1,2,3,4]))
print(is_member(3, [5,6,7]))
print('\n')

print('#12\n')
print(overlapping([1,2,3], [3,4,5]))
print(overlapping([1,2,3], [6,4,5]))
print('\n')

print('#13\n')
print(generate_n_chars(7, 'g'))