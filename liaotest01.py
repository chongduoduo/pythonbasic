# -*- coding: utf-8 -*-
import math
def quadratic(a, b, c):
    delta=pow(b,2)-4*a*c
    if delta>0:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        return (x1, x2)
    elif delta==0:
        x1=-(b/2*a)
        x2=-(b/2*a)
        return (x1, x2)
    else:
        m1=(-b/2*a)
        m2=(math.sqrt(-delta)/(2*a))
        x1=complex(m1,m2)
        x2=x1.conjugate()
        return (x1, x2)

print(quadratic(2,1,3)) 
print (a,b,c)
# 测试:
print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)
