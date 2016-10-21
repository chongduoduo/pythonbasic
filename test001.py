#mylist = [x*x for x in range(3)]
#print mylist
#for i in mylist:
#    print(i)

#mygen = (x*x for x in range(4))
#print mygen
#for i in mygen:
#    print i

#encoding = utf-8

def fib(max):
    a, b = 1, 1
    while a < max:
        yield a
        a, b = b, a+b

for n in fib(15):
    print n

m = fib(13)
print m
print m.next()
print m.next()
print m.next()