# name var and set to 10
types_of_people = 10
# Create var with string and variable embedded
x = f"There are {types_of_people} types of people."

# name vars
binary = "binary"
do_not = "don't"
#  Create var with string and variables embedded
y = f"Those who know {binary} and those who {do_not}."

#print vars
print(x)
print(y)

#print strings with vars embedded
print(f"I said: {x}")
print(f"I also said: '{y}'")

#create var and set to False
hilarious = False
#set var to string, not sure what {} does yet
joke_evaluation = "Isn't that joke so funny?! {}"

#print var and set to format of it to var hilarious, which is False? What is format(false)?
print(joke_evaluation.format(hilarious))

# create some more string vars
w = "This is the left side of..."
e = "a string with a right side."

# concatonate the two strings
print (w + e)
