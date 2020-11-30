L1= eval(input("Enter 10 numbers for list 1"))
x = int(input("Enter number to search"))
if x in L1 :
  y = L1.index(x)
  print("Value of number entered is :", x)
  print("Index of the value is :" ,y)
else:
  print("Error")