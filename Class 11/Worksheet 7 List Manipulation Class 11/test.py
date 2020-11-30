x = eval(input("Enter :"))
y = len(x) - 1
for i in range (0 ,y) :
    x[i+1] = x[i] + x[i+1]
print (x)
