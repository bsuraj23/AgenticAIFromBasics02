
Python RegEx
=============
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

RegEx Module
==============
Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:

import re

RegEx in Python
=================
When you have imported the re module, you can start using regular expressions:

Example:
Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

RegEx Functions
=================
The re module offers a set of functions that allows us to search a string for a match:

Function	          Description
*findall	     Returns a list containing all matches
*search	         Returns a Match object if there is a match anywhere in the string
*split	         Returns a list where the string has been split at each match
*sub	         Replaces one or many matches with a string

Sets
======
A set is a set of characters inside a pair of square brackets [] with a special meaning:

Set	                           Description	
[arn]	     Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	     Returns a match for any lower case character, alphabetically between a and n	
[^arn]	     Returns a match for any character EXCEPT a, r, and n	
[0123]	     Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	     Returns a match for any digit between 0 and 9	
[0-5][0-9]	 Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	 Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	         In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

