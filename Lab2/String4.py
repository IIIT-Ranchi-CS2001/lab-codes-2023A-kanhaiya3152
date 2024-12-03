def takeIn():
    myList=[]
    Name=input("Enter Name:")
    myList.append(Name)
    Roll=int(input("Enter Roll No.:"))
    myList.append(Roll)
    Marks=int(input("Enter Marks:"))
    myList.append(Marks)
    return myList

def gradePoint(marks):
    if marks<50:
        return 0
    elif marks>=50 and marks<60:
        return 6
    elif marks>=60 and marks<70:
        return 7
    elif marks>=70 and marks<80:
        return 8
    elif marks>=80 and marks<90:
        return 9
    else:
        return 10
    
    

def remarks(marks):
    if marks<50:
        return "FAIL"
    elif marks>=50 and marks<60:
        return "PASS"
    elif marks>=60 and marks<70:
        return "AVERAGE"
    elif marks>=70 and marks<80:
        return "GOOD"
    elif marks>=80 and marks<90:
        return "VERY GOOD"
    else:
        return "OUTSTANDING"

def printDetails(listing):
    print(f"Name: {listing[0]}")
    print(f"Roll Number: {listing[1]}")
    print(f"Marks: {listing[2]}")
    print(f"Grade Point: {gradePoint(listing[2])}")
    print(f"Remark: {remarks(listing[2])}")



listing=takeIn()
printDetails(listing)
