# py-ref Ver. 0.1

# Printing
print("\n") # \n makes a new line.
print("1. Printing")
print() # An empty print statement also makes a new line.
print()

print("This is a basic print function.") # This is a comment. It can go at the end of a line.
# Or a comment can go on it's own line.
print('Use single or double quotes to surround the string')
# Don't forget to put everything inside the (parenthesis) of the print function.

"""
Comments can also take up multiple lines
by using triple quotes
like this.
"""

print("""
But the triple quotes are not limited
to just comments.
It can be used with print as well
""") # Do not forget the end quotes and parenthesis.

print("""
You can also do things \
such as escape out the end of the line
if you do not want it to break.
""")

print("You can use 'single' quotes inside or escape out the \"Double\" quotes.")
print('You can not use single quotes here unless you\'ve escaped them out.')
print('You "can" use double quotes easily inside single quotes.')
print("")

text1 = ("You can assign anything to a variable. "
	"We are assigning these strings to the variable 'text'. "
	"We can also split it up between these three lines. It will treat this all like one line.")
print(text1)
print()

x = "Ha" # This is a string assigned to the variable 'x'.
print(x) # This prints the string 'x'.
print(x * 3) # This prints the contents of 'x' 3 times.
print(x * 3 + " isHaThreeTimes.")
print(x * 2 + " is Ha Three Times. " + x)
print()

print("Py" "thon")
print()

a = "Py"
b = "thon"

print("This is %s and %s, also known as %s%s." % (a,b,a,b))

formatter = "%r %r %r %r"
print(formatter % (1,2,3,4))


theName = input("What is your name?")
print("Hi", theName)


# Math
print("\n2. Math\n\n") # You can combine the line breaks into one line.

print("The number forty-two will appear over there ->", 40 + 2)
# Use a comma to separate the the two parts of this print statement.
# The first part is a string, the second part contains integers.
n = 40
print("The number", n, "is stored in 'n'. The number", n + 2, "is n + 2.")
print("The number", n, "times 2 is ", n * 2) # You can use commas to split up multiple parts.
print("The number " + str(n) + " divided by 2 is " + str(n/2)) # You can split up things like this as well.


# Lists
print("\n3. Lists\n\n")

movies = ["Avengers", "Thor", "Captain America", "Guardians of the Galaxy"]
print(movies)
print(movies[3])

# Variables
print("\n4. Variables\n\n")


# Functions
print ("\n5. Functions\n\n")


# Dictionaries
print ("\n6. Dictionaries\n\n")


