def nat():
    n=0
    while True:
        yield n
        n=n+1

def is_palindrome(n):
    return str(n)==str(n)[::-1]

def cons():
    it=nat()
    while True:
        #m=next(it)
        it=filter(is_palindrome, it)
        yield next(it)
for n in cons():
    if n < 1000:
        print(n)
    else:
        break
		
##测试
##output=filter(is_palindrome, range(1,1000))
##print(list(output))