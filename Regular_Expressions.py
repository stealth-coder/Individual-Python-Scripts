import re

"""Character    Description                                                                     Example"""

##### METACHARACTERS #####
# []	        A set of characters	                                                        "[a-m]"	
# \	        Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	        Any character (except newline character)	                                "he..o"	
# ^	        Starts with	                                                                "^hello"	
# $	        Ends with	                                                                "world$"	
# *	        Zero or more occurrences	                                                "aix*"	
# +	        One or more occurrences                                                 	"aix+"	
# {}	        Exactly the specified number of occurrences	                                "al{2}"	
# |	        Either or	                                                                "falls|stays"





##### SPECIAL SEQUENCES #####
# \A	        Returns a match if the specified characters are at the beginning of the string	                                                                    "\AThe"	
# \b	        Returns a match where the specified characters are at the beginning or at the end of a word	                                                    r"\bain"
#                                                                                                                                                                   r"ain\b"	
# \B	        Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	                                    r"\Bain"
#                                                                                                                                                                   r"ain\B"	
# \d	        Returns a match where the string contains digits (numbers from 0-9)	                                                                            "\d"	
# \D	        Returns a match where the string DOES NOT contain digits	                                                                                    "\D"	
# \s	        Returns a match where the string contains a white space character	                                                                            "\s"	
# \S	        Returns a match where the string DOES NOT contain a white space character	                                                                    "\S"	
# \w	        Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	            "\w"	
# \W	        Returns a match where the string DOES NOT contain any word characters	                                                                            "\W"	
# \Z	        Returns a match if the specified characters are at the end of the string	                                                                    "Spain\Z"


##### SETS #####
# [arn]	        Returns a match where one of the specified characters (a, r, or n) are present	
# [a-n]	        Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	Returns a match for any character EXCEPT a, r, and n	
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	        Returns a match for any digit between 0 and 9	
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

##### FUNCTIONS #####
# findall()     Returns a list containing all matches                                                       x = re.findall("Spain", text)
# search()      Searches the string for a match and returns a match object if there is a match              x = re.search("\s", text)
# split()       Returns a list where the string has been split at each match                                x = re.split("\s", text)
# sub()         Replaces the matchecs with the text of your choice                                          x = re.sub("\s", "9", text)
# span()        Returns a tuple containt the start and end position of the match                            print(x.span())
# group()       Prints the part of the string where there was a math                                        print(x.group())







text = """Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released
in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.
Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including procedural, object-oriented,
and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.

Python was conceived in the late 1980s as a successor to the ABC language. Python 2.0, released 2000, introduced features like list
comprehensions and a garbage collection system capable of collecting reference cycles. Python 3.0, released 2008, was a major revision
of the language that is not completely backward-compatible, and much Python 2 code does not run unmodified on Python 3.
Due to concern about the amount of code written for Python 2, support for Python 2.7 (the last release in the 2.x series) was extended to 2020.
Language developer Guido van Rossum shouldered sole responsibility for the project until July 2018 but now shares his leadership as a
member of a five-person steering council"""



# Find all lower case characters alphabetically between "a" and "m":
a = re.findall("[a-m]", text) 
print (a)
print ("\n\n\n")

# Find all digit characters:
b = re.findall("\d", text)
print (b)
