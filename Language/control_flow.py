#blocks delimited by indentation! (tabs or spaces)
#colon (:) used at end of lines containing control flow keywords


#if, if/else, if/elif/else
a = 0 + 0

if a == 0:
    print("zero!")
elif a < 0:
    print("negative!")
else: # else is always optional
    print("positive!")

x = 34 - 23            # A comment.
y = "Hello"            # Another one.
z = 3.45
if z == 3.45 or y == "Hello":
    x = x + 1
    y = y + "World"   # String concat.
print(x)
print(y)


mode = "absolute"
if mode == "canonical":
	miles = "canonical"
elif mode == "isomeric":
	smiles = "isomeric"
else:
	raise TypeError("unknown mode")

# multiple conditions
if (ben <= 5 and chen >= 10 or chen == 500 and ben != 5):
# range test
if (3 <= Time <= 5):


#while
a = 3
print("While loops")
while a > 0:
    print(a)
    a -= 1

x = 3
while x < 5 :
    print(x, "still in the loop")
    x+=1

# =======================================
#for loops (really a "foreach" loop) > lists, dictionnaries, ...
names = ["Ben", "Chen", "Yaqin"]
for name in names:
	print(smiles)

ages = {"Sam " :4, "Mary ":3, "Bill " :2}
for name in ages.keys():
    print(name , ages[name])


print("For loops")
for a in range(3):
    print(a) #>>0 1 2

for odd in [1, 3, 5, 7]:
    print(odd*odd)

#xrange()

print("For loops")
a = [3, 1, 4, 1, 5, 9]
for i in range(len(a)):
    print(a[i])

for someChar in "Hello World":
    print(someChar)

for (x, y) in [('a',1), ('b',2), ('c',3), ('d',4)]:
	print(x)

for i in range(5):
	print('The square of',i,' is',i*i)

for letter in "Sunday":
    print(letter)

#Common while loop idiom:
f = open(filename, "r")
while True:
    line = f.readline()
    if not line:
        break
    # do something with line

# break to stop the for loop
# continue to stop processing the current item (like in C)
#   -> stop processing the current iteration of the loop and to immediately go on to the next one
for value in [3, 1, 4, 1, 5, 9, 2]:
	print("> Checking "+ str(value))
	if value > 8:
		print("Exiting for loop")
		break
	elif value < 3:
		print("Ignoring")
		continue
	print("The square is "+ str(value**2))

#pass keyword:
if a == 0:
    pass  # do nothing
    else:
        # whatever

# Tuple assignment in for loop
data = [ ("C20H20O3", 308.371),
	("C22H20O2", 316.393),
	("C24H40N4O2", 416.6),
	("C14H25N5O3", 311.38),
	("C15H20O2", 232.3181)]
for (formula, mw) in data:
	print("The molecular weight of %s is %s" % (formula, mw))

for i in range(0, len(data), 2):
	print(data[i])
##('C20H20O3', 308.371)
##('C24H40N4O2', 416.6)
##('C15H20O2', 232.3181)


# =======================================
asserts : An assert statement will check to make sure that something is true during the course of a program.
If the condition if false, the program stops
(more accurately: the program throws an exception)

assert(number_of_players < 5)

# =======================================
try:
    <body>
except <ErrorType>:
    	<handler>



