# find the nearest number betwwen 1 to 150 
n1 = int(input("enter number 1 between 1 to 150 :"))
n2 = int(input("enter number 2 between 1 to 150:"))
if n1<150 and n1>0:
    if n2<150 and n2>0:
        if n1>n2:
            print("1st number is nearest to the number 150")
        elif n2>n1:
            print("2nd number is nearest to the number 150")
        else:
            print("both numbers are equal")
    else:
        print("enter number 2 betwwen 1 to 150")
else:
    print("enter number 1 between 1 to 150")
