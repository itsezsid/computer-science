L1= eval(input("Enter numbers for list 1"))
L2 = eval(input("Enter numbers for list 2"))
L3 = L1 + L2
L4=[]
x = int(input("Enter 1 for merge , 2 for sort , 3 for union , 4 for intersection : "))
if x == 1:
  print("Merged: " , L3)
elif x == 2:
  L3.sort()
  print("Sorted: " , L3)
elif x == 3:
  union = list(set(L1) or set(L2))
  print ("Union: " , union)
elif x == 4 :
  inter = list(set(L1) and set(L2))
  print("Intersection" ,inter)
else :
  print("Error")