#!/usr/bin/python2.7
'''

   Purpose: How to write docstring

   Docstring:In programming, a docstring is a string literal specified in

             source code that is used, like a comment, to document a specific segment of code.

   Example: build a list function in python

   Version: 1.0

   Author: Imran Ahmed

   Date: August 29th 2021

   License: GPL v2.0                 '''

 

''' string comparisons ==, !=, <, >, <=, >=  id '''

'''

    If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that.

'''

 

 

def  buildlist():

 

   alist = []

   print "\n \t \t ***Function builds a Number list & returns it *** \n"

   while True:

       item = input('Enter an element: ')

       if item eq 'exit':

 

            break

 

       else:

            alist.append(item)

 

   return alist

 

 

mylist = buildlist()

print "The list we built is: %s " % mylist

 

if __name__ == 'main':

 

     main()