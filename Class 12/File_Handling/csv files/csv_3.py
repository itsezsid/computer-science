import csv
from tabulate import tabulate
file = open('Q3.CSV', 'w')
writefile = csv.writer(file)
n = int(input("ENTER THE NO. OF RECORDS: "))
for i in range(n):
    fn = input("ENTER YOUR FIRST NAME: ")
    ln = input("ENTER YOUR LAST NAME: ")
    d = input('ENTER YOUR DAY OF BIRTH: ')
    m = input('ENTER YOUR MONTH OF BIRTH: ')
    y = input('ENTER YOUR YEAR OF BIRTH: ')
    dob = d+'/'+m+'/'+y
    age = (2020-int(y))
    writefile.writerow([fn, ln, dob, age])
file.close()
file = open("Q3.CSV", 'r')
read_file = csv.reader(file)
lst = []
for i in read_file:
    lst.append(i)
print("THE ORIGINAL LIST IS:")
print(tabulate(lst, headers=['FIRST NAME',
                             'LAST NAME', 'DATE OF BIRTH', 'AGE']))
file.close()


file = open("Q3.CSV", 'r')
read_file = csv.reader(file)
lst1 = []
for i in read_file:
    if i != []:
        if i[1][0] == 'M' or i[1][0] == 'P':
            lst1.append(i)
print("THE LIST WHOSE LAST NAME STARTS WITH M OR P: ")
print(tabulate(lst1, headers=['FIRST NAME',
                              'LAST NAME', 'DATE OF BIRTH', 'AGE']))
file.close()


file = open("Q3.CSV", 'r')
read_file = csv.reader(file)
lst2 = []
for i in read_file:
    if i not in lst2:
        lst2.append(i)
print("THE LIST AFTER REMOVING THE DUPLICATE ENTRIES IS: ")
print(tabulate(lst2, headers=['FIRST NAME',
                              'LAST NAME', 'DATE OF BIRTH', 'AGE']))
file.close()


file = open("Q3.CSV", 'r')
read_file = csv.reader(file)
for i in range(len(lst)//2):
    lst.remove([])
l = len(lst)
for i in range(0, l):
    for j in range(0, l-i-1):
        if (lst[j][3] > lst[j + 1][3]):
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print("THE LIST AFTER SORTING IS: ")
print(tabulate(lst, headers=['FIRST NAME',
                             'LAST NAME', 'DATE OF BIRTH', 'AGE']))
file.close()
