def count():
    fs = []
    for i in range(1, 4):
        #print("a:",i)
        def f():
            #print("func:",i)
            return i*i
        #print("b:",i)
        fs.append(f)
        print(fs)
    return fs

f1, f2, f3 = count()

print("f1=",f1())
print("f2=",f2())
print("f3=",f3())

def count2():
    def fc(j):
        def g():
            print("j=", j)
            return j*j
        return g
    fy = []
    for i in range(1,4):
        print("i=",i)
        fy.append(fc(i))
        print(fy)
    return fy

fc1, fc2, fc3 = count2()

print("fc1=",fc1())
print("fc2=",fc2())
print("fc3=",fc3())
