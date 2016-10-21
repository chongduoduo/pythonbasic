tabby_cat = "\tI'm tabbed in."  ###\t means tabbed first.
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

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

for i in ["/", "-", "|", "\\", "|"]:
  print "%s\r" % i   
  ### if I add a comma after the double-quotes, it will not display any signs.
  ### but if I don't add the comma, all signs will be displayed. 
  ### So, what is the "\r" used for? Answer: RETURN

print "%s" % tabby_cat  ### this will display:     I'm tabbed in.
print "%r" % tabby_cat  ### this will display:"\tI'm tabbed in."

#### so create a new variable: 
test_001 = "test001"

print "%r" % test_001   ### this will display: 'test001'   (a pair of single-quotes included)
print "%s" % test_001   ### this will display:test001 (no single-quotes)

test_002 = '''test"002'''

print "%r" % test_002 ### this will display: 'test"002'
print "%s" % test_002 ### this will display: test"002

test_003 = "test'003"

print "%r" % test_003 ### this will display: "test'003"
print "%s" % test_003 ### this will display: test'003

###summary:That's because %r is printing out the raw representation of what you typed, which is going to include the original escape sequences. Use %s instead. Always remember this: %r is for debugging, %s is for displaying.