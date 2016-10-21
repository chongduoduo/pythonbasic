from sys import argv
from os.path import exists  ##get exists feature from os.path package

script, from_file, to_file = argv  ## unpack the argv

print "Copying from %s to %s" %(from_file, to_file) ## a note 

##we could do these two on one line, how?
in_file = open(from_file) #open the from_file
indata = in_file.read() #store the data of from_file to indata

print "The input file is %d bytes long" % len(indata)  ## display the length of from_file

print "Does the output file exist? %r" % exists(to_file) ## a note to judge if the to_file exists or not
#print "Ready, hit RETURN to continue, CTRL-C to abort." ## a note
#raw_input()  ## let user input something

out_file = open(to_file, 'w') ## empty the to_file and open it with w mode
out_file.write(indata) ## write the content of from_file to to_file

print "Alright, all done." ## a note telling user finishing.

out_file.close()  ## save and close the to_file
in_file.close() ##save and close the from_file  please note: use the in_file for closing, not to_file.