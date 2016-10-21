from sys import argv  ##call the argv feature

script, filename = argv  ##unpack the argv. user should input the script name and the file name 

print "We're going to erase %r." % filename   ## a note to user for empty the file named filename
print "If you don't want that, hit CTRL-C (^C)." ##CTRL-C means: don't run the script and exit directly
print "If you do want that, hit RETURN."  ## continue to run the script

raw_input("?") ##let user input exit or continue

print "Opening the file ..."  ## a note
target = open (filename, 'w') ## open the file with writing function, and save it into a variable named "target"

print "Truncating the file. Goodbye!" ## a note
target.truncate()  ## erase the target(the file) 

print "Now I'm going to ask you for three lines." ## a note

line1 = raw_input("line 1: ") ## let user input anything in one line
line2 = raw_input("line 2: ") ## see above
line3 = raw_input("line 3: ") ## see above

print "I'm going to write these to the file."  ## a note to user for writing something new

#target.write(line1) ## write something into the file(target) automatically
#target.write("\n")  ## input a Enter sign
#target.write(line2) ## see above
#target.write("\n")
#target.write(line3)
#target.write("\n")
string1 = "%s\n%s\n%s\n" %(line1, line2, line3)
target.write(string1) 

print "And finally, we close it." ## a note to tell user close the file.
target.close()  ## close and save the file.

raw_input("Now let's verify the file content.PRESS ENTER")
readfile = open(filename)
##content = readfile.read()
print(readfile.read())

print "Close the file."
readfile.close()
