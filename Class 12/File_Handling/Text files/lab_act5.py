myfile = open("Q5.txt", "w")  # for creating file
n = int(input("enter number of lines"))
# to enter text in the file
for i in range(n):
    txt = input("enter the lines of text for the file ")
    myfile.write(txt)
    myfile.write("\n")
myfile.close()

myfile1 = open("Q5.txt", "r")
str1 = myfile1.readlines()
no_4l = 0
cd = 0
cs = 0

print(str1)
for i in str1:
    i = i.rstrip('\n')
    a = i.split()
    for j in a:
        if j.isalpha() and len(j) == 4:
            no_4l += 1
    for j in range(len(i)):
        if i[j].isspace() == False and i[j].isalpha() == False:
            if i[j].isdigit():
                cd += 1
            else:
                cs += 1
print("the number of 4 digit words is ", no_4l)
print("the number of digits ", cd)
print("the number of symbols ", cs)
