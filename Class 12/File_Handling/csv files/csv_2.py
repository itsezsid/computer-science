import csv
with open(r"static\csv2.csv", 'w') as csv2:
    filewriter = csv.writer(csv2, delimiter="|")
    filewriter.writerow(['Name', 'Score', "Attempts", "Qualify"])
    filewriter.writerow(["Anastasia", 12.5, 1, "yes"])
    filewriter.writerow(["Dima", 9, 3, "no"])
    filewriter.writerow(["Katherine", 16.5, 2, "yes"])
    filewriter.writerow(["James", 0, 3, "no"])
    filewriter.writerow(["Emily", 9, 2, "no"])
    filewriter.writerow(["Michael", 20, 3, "yes"])
    filewriter.writerow(["Matthew", 14.5, 1, "yes"])
    filewriter.writerow(["Laura", 0, 1, "no"])
    filewriter.writerow(["Kevin", 8, 2, "no"])
    filewriter.writerow(["Jonas", 19, 1, "yes"])


with open(r"static\csv2.csv", 'r') as csv2:
    filereader = csv.reader(csv2)
    rowlist = [row for row in filereader if row]
    avg = 0
    for i in range(1, len(rowlist)):
        row2 = rowlist[i][0].split("|")
        avg += float(row2[1])*float(row2[2])
    avg = avg/len(rowlist)
    print("The average score is", avg)

with open(r"static\csv2.csv", 'r') as csv2:
    filereader = csv.reader(csv2)
    rowlist = [row for row in filereader if row]
    newrowlist = []
    for i in range(len(rowlist)):
        row2 = rowlist[i][0].split("|")
        if row2[1] == '0':
            row2[1] = "None"
        newrowlist.append(row2)
with open(r"static\csv2.csv", 'w') as csv2:
    filereader = csv.writer(csv2, delimiter="|")
    for row in newrowlist:
        filereader.writerow(row)


with open(r"static\csv2.csv", 'r') as csv2:
    filereader = csv.reader(csv2)
    rowlist = [row[0].split("|") for row in filereader if row]
    newrowlist = []
    for i in range(4):
        newrow = []
        for j in range(11):
            newrow.append(rowlist[j][i])
        newrowlist.append(newrow)
    print("Transpose of data:")
    for row in newrowlist:
        print(row)

for row in rowlist:
    rowlist.append(row)
