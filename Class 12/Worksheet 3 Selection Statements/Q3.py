x = int(input("Enter your number\n"))
if x > 0:
    if x%2 ==0:
        print("Number is positive and even")
    else:
        print("Number is positive and odd")
elif x < 0:
    if x%2 == 0:
        print("Number is negative and even")
    else :
        print("Number is negative and odd")
else:
    print("Number is zero")