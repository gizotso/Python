# Python
#=================================
# dynamically typed
# - Variables come into existence when first assigned to
#  variable can refer to an object of any type
# All types are (almost) treated the same way
# Main drawback: type errors are only caught at runtime

#=================================
Integers: 2323, 3234L
Floating Point: 32.3, 3.1E2
Complex: 3 + 2j, 1j

1/3 = 0 # python 2.x
1/3 = 0.33333333 # python 3.x  (or 1./3 force float !)

Sequence types : tuples (...), lists [...] and strings
MemoryError collection type Dictionaries

# True and False are constants in Python
# Other values equivalent to True and False
#    -False: False, zero (0, 0.0, 0j), None, empty container or object ("", [], {}, (), ...)
#    -True: True, non-zero numbers, non-empty objects

#Essentially,anything that was a 0 value (the integer or floating point 0, an empty string "", or an empty list []) was False, and everything else was true.
bool("a") ## True
bool(1)  ##True  bool(-1)
bool(0)  ##False
bool([]) ##False

#=================================
#  Logical evaluation
#================================
# comparison
# x == y  x and have same value
# x is y  x and y are 2 variables that refer to the identical same object.


3 < 4   #>>> True
1 == 2  #>>> False
1 is 2  #>>> False
1 is 1  #>>> True

'a' < 'b'  #>>> True
'A' < 'a'  #>>> True

1<2<3  #>>> True
1<2<1  #>>> False

[1,2,3] == [1,2,4] #>>> False

# multiple comparison
hours = 5
0 < hours < 24  #>>> True

"""
Boolean algebra
a and false == false    - a * 0 = 0
a and true == a         - a * 1 = 1
a or false == a         - a + 0 = a
a or true  == true
"""
# Boolean Expressions as Decisions
# and and or dont return True or False
# They return the value of one of their sub-expressions (which may be a non-Boolean value).
# lazy evaluation
x=2 y=3 z=4
x or  y  #>>>2   If x is true, return x. Otherwise, return y.
x and y  #>>>3   If x is false, return x. Otherwise, return y.

0 and 2 #>>> 0
2 and 0 #>>> 0
0 or 1  #>>> 1
0 or  2 #>>> 2
2 or  0 #>>> 2
0 or  0 #>>> 0

1 and 2 and 3 #>>> 3 < if all false : last item evaluated is returned
1 and 0 and 3 #>>> 0 < returns value of 1st false
1 or  2 or  3 #>>> 1
0 or  0 or  3 #>>> 3 < returns value of 1st true (if al false returns last)
# => old and-or deprecated trick : result = test and expr1 or expr2 (warning if expr1 is false)

#conditional expressions (python >2.5)
x = (true_value if condition else false_value)

flavor = input("What flavor do you want [vanilla]:" ) or "vanilla"
# in case input is left empty which is flase default value vanilla will be used

#=================================
# Strings
# immutable
#=================================
s="tom's cat"
x='tom\'s cat' #idem

#Use triple double-quotes for multi-line strings or strings than contain both ' and " inside of them:
"""a ' "b c"""

#concatenation
"hello" + "world"	#'helloworld'
# repetition
"hello"*3		#"hellohellohello"
(3 * "spam") + ("eggs" * 5) # 'spamspamspameggseggseggseggseggs'
# indexing & slicing
"hello"[0]		#"h"
"hello"[-1]		#"o"		# (from end)
"hello"[1:4]	#"ell"		# slicing <string>[<start>:<end>] but
                            # end position is not included !
"hello"[1:]		#"ello"
"hello"[:3]     #"hel"
"hello"[:]		#"hello"
"hello"[1:-2]   #"el"  #idx=1 to idx=-2
Bonjour[1:6:2]  #'oju'
#size
len("hello")		#5
# comparison
"hello" < "jello"	#True
# search
"e" in "hello"		#True
#New line : \n
str = "Have \n a good day
print(str)
#Line continuation: triple quotes
>>> str="""this is a long
test
so i use triple quotes"""
>>> str
'this is a long\ntest\nso i use triple quotes'
#len(str) = 42

"32,24,25,57".split(",")
#['32', '24', '25', '57']

# Strings share many features with list
smiles = "C(=N)(N)N.C(=O)(O)O"
smiles[0]    #'C'
smiles[1:3]  #'(='
smiles.find("(O)")
smiles.find(".", 10) # starts the lookup at pos 10
smiles.split(".")    # ['C(=N)(N)N', 'C(=O)(O)O']

# string operator : IN, NOT IN
if "Br" in "Brother":
	print ...
email_address = "clin"
if "@" not in email_address:
	email_address += "@brandeis.edu"


# strip, rstrip, lstrip are ways to remove whitespace or selected characters
#  => uset it to strip off final newlines from lines read from files
# lstrip : leading whitespace removed
# rstrip :  trailing whitespace removed
line = " # This is a comment line \n"
line.strip()
## '# This is a comment line'
line.rstrip()
## ' # This is a comment line'
line.rstrip("\n")


# Other functions
email_address.startswith("c")  ## True
email_address.endsswith("c")  ## False
capitalize, lower, upper
title
center, ljust, rjust
"abca".count("a")      #2
"this,is,it".find(",") #4 - rfind (returns the right most pos)
"Mr x, Mr toto".replace("Mr","Sir") # 'Sir x, Sir toto'


# substitution
"%s@brandeis.edu" % "clin"
##'clin@brandeis.edu'

names = ["Ben", "Chen", "Yaqin"]
", ".join(names)
##'Ben, Chen, Yaqin'
"x".join(names)
## 'BenxChenxYaqin'

"hello".upper()
## 'HELLO'

s = "andrew
s[0]='b' ## TypeError: 'str' object does not support item assignment
s = "A" + s[1:] ## 'Andrew'

# warning : strings are "Read-Only"
s = "andrew"

type(s)
##<type 'str'>

#conversion
str(8), str(3.14)

'hello' + str(2) # str() func can convert an instance of any data type into a string

# iteration through chars
for ch in "Hellow World!":
	print (ch, end="x")

ord("A") #65 : ordinal of a 1 char string
chr(65)  #'A'

eval("8")*2 # Evaluate string as an expression

WARNING
>>> x = 'abc'
>>> x[1]
'b'
>>> x[1]='g'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

#=================================
# Lists [...]
# -compound data type
# -sequences of arbitrary values !
# -Mutable, meaning they can be changed. Strings can not be changed
# -index starts @0
#================================
# compound data type
 a = [1, 2, 'blue']
 a
 print(a)
 a[0]  # !! index starts at 0
 a[-1] # 'blue'  Negative index go backwards from the last element

a = [1, 2, 3, 4, 5]
a = [1, 2] + [3, 4, 5] ## [1, 2, 3, 4, 5]
len(a) # number of elts > 5
a = [1, 2] * 5 ## [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

#add an elt
a.append(6) #a = [1, 2, 3, 4, 5, 6]
a = a + [6] #a = [1, 2, 3, 4, 5, 6]   + creates a fresh list with a new memory ref
a = [1, 2, 3, 4, 5]
a.insert(2,'i') #a = [1, 2, 'i', 3, 4, 5]  added elet before the third item
a.extend([6,7,8]) #a=[1, 2, 3, 4, 5, 6, 7, 8]  extend operates on list a in place

a = [99, "bottles of beer", ["on", "the", "wall"]]
a[2][2] #> 'wall'

#Item and slice assignment
a[0] = 98
a[1:2] = ["bottles", "of", "beer"] #a = [98, "bottles", "of", "beer", ["on", "the", "wall"]]
#remove last elet
del a[-1]	#[98, "bottles", "of", "beer"]
# remove an elt
a = [1, 2, 3, 4, 5]
del a[2] #[1, 2, 4, 5]


numbers = range(0,20)
evens = numbers[2::2] #slice starts at2, by step of 2


#range() built-in that generates sequences of numbers starting with 0
# -> use list(range()) to turn sequence into an explicit list

range(5,10)     # [5,6,7,8,9]
range(0, 10, 2) #  [0,2,4,6,8]
a = range(5)	# [0,1,2,3,4]
list(a)

a.append(5)		# [0,1,2,3,4,5]
#remove elet (last by default)
a.pop()			# [0,1,2,3,4]
5
a.insert(0, 5.5)		# [5.5,0,1,2,3,4]
a.pop(0)			# [0,1,2,3,4]
5.5
a.reverse()			# [4,3,2,1,0]
a.sort()			# [0,1,2,3,4]


 a = [1, "blue"]
 a[1] = 2
#>[1, 2]
 x.extend("red")
 [1, 2, 'blue', 'r', 'e', 'd']


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
months[n-1]
# lists are mutable
months[0] = "January"

days_of_the_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
days_of_the_week[2] ##'Tuesday'


# ===== operations ===============
# - <list>.append(x), <list>.insert(i,x), <list>.index(x), <list>.count(), <list>.sort(), <list>.reverse(), <list>.remove(), <list>.pop(i), <list>.extend(x)
# - Indexing L[i], Slicing	L[1:5], Concatenation L + L
# - Repetition L * 5,
# - Membership test 'a' in L
Length len(L)

li = ['a', 'b', 'c', 'b']
li.index('c') #>>>2
li.count('b')
li.remove('b') #remove 1st occurence

# nested list
s = [1,2,3]
t = ['begin', s, 'end']
t #>>> ['begin', [1, 2, 3], 'end']
t[1][1] #>>> 2

#=================================
#  Dictionaries(maps) : Refer value through key; "associative arrays" / Mappings
#  => Lookup table key->value
#================================
# - Keys must be immutable (numbers, strings, frozen set, tuples of immutables -> these cannot be changed after creation)
# - Duplicate keys are not allowed (duplicate values are ok)
# - Keys will be listed in arbitrary order

d = { "foo" : 1, "bar" : 2 }
print(d["bar"])   #>>> 2

d = { 1:10, 2:15}
d[1] #>>>10


d={'alice':1234, 'bob':5678, 'clare':9012}
d['bob']  #>>> 5678
# accessor methods
d.keys()   #>>>dict_keys(['clare', 'bob', 'alice'])
d.values() #>>>dict_values([9012, 5678, 1234])
d.items()  #>>>dict_items([('clare', 9012), ('bob', 5678), ('alice', 1234)])
d['alice']=0   #>>>{'alice': 0, 'bob': 5678, 'clare': 9012}
del d['alice'] #>>>{'bob': 5678, 'clare': 9012}

some_dict = {}
some_dict["foo"] = "yow!"
print(some_dict.keys()) #>>> dict_keys(['foo'])
#remove 1 elt
del d['bob'] #>>>d {'alice': 1234, 'clare': 9012}
d.clear()    "remove all elts"

symbol_to_name = {
	"H": "hydrogen",
	"He": "helium",
	"Li": "lithium",
	"C": "carbon",
	"O": "oxygen",
	"N": "nitrogen"
}

symbol_to_name["C"]                          ## 'carbon'
"O" in symbol_to_name, "U" in symbol_to_name ## (True, False)
"oxygen" in symbol_to_name                   ## False
symbol_to_name["P"]                          ## KeyError: 'P' > lookup failure raises an exception
symbol_to_name.get("P", "unknown")           ## 'unknown'     > use get
symbol_to_name.get("C", "unknown")           ## 'carbon'
symbol_to_name.keys()                        ## dict_keys(['H', 'He', 'N', 'O', 'Li', 'C'])
symbol_to_name.values()                      ## dict_values(['hydrogen', 'helium', 'nitrogen', 'oxygen', 'lithium', 'carbon'])
symbol_to_name.update( {"P": "phosphorous", "S": "sulfur"} )
del symbol_to_name['C']

# python 2
dic.itervalues()
dic.iterkeys()
dic.iteritems()


atomic_number_to_name = {
	1: "hydrogen"
	6: "carbon",
	7: "nitrogen"
	8: "oxygen",
}
nobel_prize_winners = {
(1979, "physics"): ["Glashow", "Salam", "Weinberg"],
(1962, "chemistry"): ["Hodgkin"],
(1984, "biology"): ["McClintock"],
}


#convenient way to create dictionaries without having to quote the keys
ages = {"Rick": 46, "Bob": 86, "Fred": 21}
dict(Rick=46, Bob=86, Fred=20)

# ===== operations ===============
keys(), values(), items()
has_key(key)
clear(), copy()
get(key[,x])
setdefault(key[,x])
update(D), popitem()


#=================================
#  Tuple (...) : ~read only array
# - immutable
#================================
t = (1, 2, 3, 4) # ! use of rounded bracket ()
t[1]    #>>>2   2nd item in the tuple
t[-1]   #>>>4   last item
t[0:2]  #>>>(1, 2) from item 0 to item 2-1 (2 is excluded)
t[2:-1] #>>>(3,)   from 2 to last-1
t[1:]   #>>>(2, 3, 4)


3 in t #>>> True
(1, 2, 3) + (4, 5, 6) #>>> (1, 2, 3, 4, 5, 6)

tu = (23, 'abc', 4.56, (2,3), 'def')

yellow = (255, 255, 0) # rgb
yellow[1:] # (255, 0)
yellow[0] = 0
# TypeError: 'tuple' object does not support item assignment

# useful in string interpolation
"%s lives in %s at latitude %.1f" % ("Andrew", "Sweden", 57.7056)
## 'Andrew lives in Sweden at latitude 57.7'

names = ['ben', 'chen', 'yaqin']
gender = [0, 0, 1]
zip(names, gender)
# [('ben', 0), ('chen', 0), ('yaqin', 1)]

positions = [ ('Bob',0.0,21.0),
              ('Cat',2.5,13.1),
              ('Dog',33.0,1.2)
            ]


# ===== operations ===============
Indexing		e.g., T[i]
Slicing			e.g., T[1:5]
Concatenation	e.g., T + T
Repetition		e.g., T * 5
Membership test	e.g., i in T
Length			e.g., len(T)

#=================================
#  Print & Format
#================================
# print automatically adds a newline to the end of the string.
# tip : use print('hello' , ) will not adds the eol


"Hello {0} {1}, you may have won ${2}" .format("Mr.", "Smith", 10000)
"Hello {} {}, you may have won ${}" .format("Mr.", "Smith", 10000)
#>>>'Hello Mr. Smith, you may have won $10000'


'This int, {0:5}, was placed in a field of width 5'.format(7)
#>>>'This int,     7, was placed in a field of width 5'

'This int, {0:10}, was placed in a field of witdh 10'.format(10)
#>>>'This int,         10, was placed in a field of witdh 10'

'This float, {0:10.5}, has width 10 and precision 5.'.format(3.1415926)
#>>>'This float,    3.1416, has width 10 and precision 5.'

'This float, {0:10.5f},  is fixed at 5 decimal places.'.format(3.1415926)
#>>>'This float,   3.14159, has width 0 and precision 5.'

"left justification: {0:<5}.format("Hi!")
#>>>'left justification: Hi!  '
"right justification: {0:>5}.format("Hi!")
#>>>'right justification:   Hi!'
"centered: {0:^5}".format("Hi!")
#>>>'centered:  Hi!


# <template-string>.format(<values>)
# {} within the template-string mark into which the values are inserted.
# Each slot has description that includes format specifier telling Python how the value for the slot should appear.
# format specifier : <width>.<precision><type>
#     f means "fixed point" number
#     <width> tells us how many spaces to use to display the value. 0 means to use as much space as necessary.
#     <precision> is the number of decimal places
total = 1.5
print("The total value of your change is ${0:0.2f}".format(total))
##The total value of your change is $1.50

"Hello {0} {1}, you may have won ${2}" .format("Mr.", "Smith", 10000)
##'Hello Mr. Smith, you may have won $10000'

'This int, {0:5}, was placed in a field of width 5'.format(7)
##'This int,     7, was placed in a field of width 5'
## note right justification for num values
'This int, {0:10}, was placed in a field of witdh 10'.format(10)
##'This int,         10, was placed in a field of witdh 10'
'This float, {0:10.5}, has width 10 and precision 5.'.format(3.1415926)
##'This float,    3.1416, has width 10 and precision 5.'
'This float, {0:10.5f},  is fixed at 5 decimal places.'.format(3.1415926)
##'This float,   3.14159, has width 0 and precision 5.'

# justification <, >, ^
"left justification: {0:<5}".format('Hi!')
##'left justification: Hi!  '
"right justification: {0:>5}".format("Hi!")
##'right justification:   Hi!'
"centered: {0:^5}".format("Hi!")
'centered:  Hi! '




1/2 # 0 in Py2.xx => 0.5 in Py3.xx
float(1)/2 #0.5

i = 10
d = 3.1415926
s = "I am a string!"
print("%d\t%f\t%s" % (i, d, s))
##10	3.141593	I am a string!

print("%s => %d" % ('week', 45))
## week => 45

x=1
y=2
x,y = y,x # swapping values !


float(22//5)   4.0
int(4.5)       4
int(3.9)       3
round(3.9)     4
round(3)


http://stackoverflow.com/questions/13890935/timestamp-python

import datetime
print datetime.datetime.utcnow()
str(datetime.datetime.now())
