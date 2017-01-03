days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
# Comma suppresses newlines but does it work when the string contains \n or 
# Just between the two stings? The answer is no the \n's are not suppressed.
# Just the one after months: 
print "Here are the months: ", months

# Presumably this just allows me to type in text as written
# Between the three quotes.
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

