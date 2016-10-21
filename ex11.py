print "How old are you?",
age = raw_input()   ###raw_input() will return a string, input() will return a int or float value.
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight =raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

##anid = raw_input("Input your id please!")  ### user can input the content after the note "Input your id please."
##print "your id is %s" % anid
###The input() function will try to convert things you enter as if they were Python code, but it has security problems so you should avoid it.
###So if you want to input a number, rather than a string, please use int(raw_input())