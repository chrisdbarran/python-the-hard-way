from sys import argv
from os.path import exists


script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# Load data in in one line
indata = open(from_file).read()

# Calculate the length of the  data
print "The input file is %d bytes long" % len(indata)

# Check if the output file exists
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# write the data out in one line
out_file = open(to_file, 'w')
out_file.write(indata)


print "Alright, all done."
out_file.close()
