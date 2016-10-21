from sys import argv

script, input_file = argv

def print_all(f):  ###a function reading the whole content of a file
    print f.read()

def rewind(f):  ## let the printer come back to the top of a file
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline() 
	## first, print the line number(actually the line_acount value)
	## second, print the line that cursor located in a file
	## third, the cursor position +1 line

current_file = open(input_file)

print "First let's print the whole file:\n"
print (current_file.tell())
print_all(current_file)
print (current_file.tell())
print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file) 
## note: the current_line just help the people watching the result to identify the line number, not the program.
## the program will decide which line should be printed by printer

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

print (current_file.tell()) 

print "use readlines()"
rewind(current_file)
print (current_file.readlines())
print (current_file.tell())


