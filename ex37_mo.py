try:
    a = 1 / 2
    print a
    print m
    b = 1 / 0
    print b
    c = 2 / 1
    print c
except NameError:
    print "Ops!!"
except ZeroDivisionError:
    print "Wrong math!!"
except:
    print "Error"
else:
    print "No error! yeah!"
finally:
    print "Successfully!" 
	

class Person:
    def sayhi(self):
        print "Hello guys!"

p = Person()
p.sayhi()
print (dir(p))