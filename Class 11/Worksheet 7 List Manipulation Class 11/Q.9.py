L1 = eval(input("Enter list: "))
ran = int(input(("Enter range: ")))
L2 = []
for i in range(0, ran):
    if L1[i] ** 1 / 2 == i:
        sum = 0
        while (L1[i] != 0):
            sum = sum + int(L1[i] % 10)
            L1[i] = int(L1[i] / 10)
        if sum < 10:
            L2.append(L1[i])
            print(L2)
        