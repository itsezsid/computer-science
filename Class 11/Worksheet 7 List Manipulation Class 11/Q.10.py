num = eval(input("Enter numbers for list"))
k = num.pop(0)
x = num.pop(len(list())-1)
num.insert(0 , x)
num.append(k)
print(num)
