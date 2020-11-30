L = eval(input("Enter List: "))
even = []
odd = []
for i in range (0 , len(L)):
    if L[i] % 2 == 0:
        even.append(L[i])
    else:
        odd.append(L[i])
print("Odd: ", odd , "Even: " , even)
