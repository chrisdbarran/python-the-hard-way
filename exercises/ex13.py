from sys import argv
# From the sys module include the function argv


# Create four variables and assign them the values
# From argv, namely the name of the script and the
# first three arguments.
# Will throw and error if the number of arguments doesn't match
script, first, second, third = argv

print "The script is called::", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third