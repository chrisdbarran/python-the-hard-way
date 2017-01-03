from sys import argv

# Get the name of the filename passed on the command line.
script, filename = argv

# Print the instructions
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#Wait for the command If return is entered then continue
raw_input("?")

# Open the file for writing.
print "Opening the file..."
target = open(filename, 'w')

# Remove any contents.
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

# Get three lines of content.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# Write them to a file adding a new line at the end.
target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

# Close the file.
print "And finally, we close it."
target.close()
