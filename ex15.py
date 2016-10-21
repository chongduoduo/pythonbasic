from sys import argv   ## calling the argv

script, filename = argv  ## unpacking argv: two arguments

txt = open (filename)  ## opening a file named filename

print "Here's your file %r:" % filename  ## a notice to user
print txt.read()  ## print the file content

#print "Type the filename again:"  ## a notice about asking user to input the filename again
#file_again = raw_input (">")  ## input line
file_again = raw_input ("Type the filename again>")
txt_again = open(file_again)  ## opening the file named file_again

print txt_again.read()  ## print the file content


