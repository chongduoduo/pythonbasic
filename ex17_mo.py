from sys import argv

###for copying a file from one to another
script, from_file, to_file = argv
indata = open(from_file).read()
outdata = open(to_file,'w').write(indata)
###once the copy run in one line, python will close the file automatically. you don't need to do close()