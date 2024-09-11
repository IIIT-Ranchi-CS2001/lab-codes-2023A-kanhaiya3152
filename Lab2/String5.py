import math
a=int(input("First number "))
b=int(input("second number "))
c=int(input("third number "))

d=(b**2)-(4*a*c)


if d==0:
    r1=(-b)/(2*a)
    r2=(-b)/(2*a)
    print("Root1: ",r1)
    print("Root2: ",r2)
elif d>0:
    r1=((-b+(math.sqrt(d)))/(2*a))
    r2=((-b-(math.sqrt(d)))/(2*a))
    print("Root1: ",r1)
    print("Root2: ",r2)
else:
    real_root=(-b)/(2*a)
    complex_root=(math.sqrt(-d)/(2*a))
    # ans=complex(real_root,complex_root)
    # print(ans)
    print("Real Root: ",real_root)
    print("Imaginary Root: ",complex_root)