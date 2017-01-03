from sys import argv

script, filename = argv

# Use the open function  to open a file
txt = open (filename)

# Print the name of the file passed on the command line.
print "Here's your file %r:" % filename
# print the contexts of the file
print txt.read()
txt.close()

# Prompt for the filename 
print "Type the filename again:"
file_again = raw_input("> ")

# Open the file again
txt_again = open(file_again)

# Print the contents of the file again
print txt_again.read()

txt_again.close()