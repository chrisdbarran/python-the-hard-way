# Short version of exercise 17
from sys import argv
script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)
# Read and write the data out in one line
open(to_file, 'w').write(open(from_file).read())
print "Alright, all done."