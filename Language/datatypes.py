# Python
#=================================
dynamically typed
- Variables come into existence when first assigned to
 variable can refer to an object of any type
All types are (almost) treated the same way
Main drawback: type errors are only caught at runtime

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
