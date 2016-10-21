
numbers = []
def print_new_list(i, max, sup):
    while i < max:
        print "At the top i is %d" %i
        numbers.append(i)

        i = i + sup
        print "Numbers now:", numbers
        print "At the bottom i is %d" %i


print_new_list(0,6,1)		
print "The numbers:"

for num in numbers:
    print num	

newnumbers = []
def print_2_list(i, max):
    for i in range(i,max):
        print "At the top i is %d" %i
        newnumbers.append(i)
        print "Numbers now:", newnumbers

print_2_list(0,6)
print "The number:"
print newnumbers
