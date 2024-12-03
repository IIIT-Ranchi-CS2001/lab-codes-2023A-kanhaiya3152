import math
a=float(input("first side of triangle: "))
b=float(input("second side of triangle: "))
c=float(input("third side of triangle: "))

val1=((b*b)+(c*c)-(a*a))/(2*b*c)
val2=((a*a)+(c*c)-(b*b))/(2*a*c)
val3=((b*b)+(a*a)-(c*c))/(2*b*a)

# print("value 1c ",val1)
angle1=math.acos(val1)
angle2=math.acos(val2)
angle3=math.acos(val3)


print("perimeter of triangle is: ",(a+b+c))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of triangle is: ",area)


print("angle of given sides of is : ",angle1*180/math.pi," ",angle2*180/math.pi," ",angle3*180/math.pi)

