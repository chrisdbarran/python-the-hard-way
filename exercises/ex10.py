# Put in a tab
tabby_cat = "\tI'm tabbed in."
# Put in a newline
persian_cat = "I'm split\non a line."
# Put in a backslash
backslash_cat = "I'm \\ a \\ cat."

# Escape sequences work inside tripple quotes
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""


print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
   for i in ["/","-","|",,"\\","|"]:
      print "%s\r" % i,