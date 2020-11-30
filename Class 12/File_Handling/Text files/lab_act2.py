def remove(file1, file2, n):
    myfile1 = open(file1, "r")
    myfile2 = open(file2, "w")
    for i in range(1, n+1):
        a = myfile1.readline()
        x = a.split()
        y = x[::]
        for i in x:
            if i in ["a", "an", "the"]:
                y.remove(i)
                index = index(i)
                y[index] = " "
        myfile2.writelines(y)
    myfile2.close()


