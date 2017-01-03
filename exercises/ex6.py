# Ten is put inside the string and assigned to value x but ten is not a string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

# The variables binary and do_not are put inside the string and assigned to y.
# binary and do_not are strings = 2.
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# The value of x which is a string is placed inside the anonymous string and printed. 3
print "I said: %r." % x
# The value of y which is a string is placed inside the anonymous String and printed. 4
print "I also said: '%s'." % y

# The boolean variable hilarious is asigned the false value and this is represented in the 
# String assiged to joke_evaluation.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# w and e are concatenated. that is combined into one longer string before being passed as an 
# argument to the print statement (python 2 print is a statement). 
# This is different to print w, e which is suppressing the new line.
print w + e

# Statements don't evaluate to anything so you can't assign them to a variable. Other 
# statements include while, if, for import etc.