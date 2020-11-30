import csv
with open("csv_file.csv", 'w', newline='') as csv_file:
    write_to_file = csv.writer(csv_file, delimiter="|")
    write_to_file.writerow(['Amount', 'Average', 'People'])
    write_to_file.writerow(['279000', str(279000//15), '15'])
    write_to_file.writerow(['396800', str(396800//36), '36'])
    write_to_file.writerow(['563000', str(563000//44), '44'])
    write_to_file.writerow(['150000', str(150000//19), '19'])
    write_to_file.writerow(['716200', str(716200//58), '58'])


reader = []
with open('csv_file.csv', 'r') as file:
    reader_csv = csv.reader(file)
    for row in reader_csv:
        reader.append(row)
        print(row)

print()

print('the first row is ', list(reader)[0])
print('the last row is ', list(reader[-1]))


print()

print('The new table with entries having less than 20 people removed is : ')
print()
reader_updated = reader[::]
for i in reader:
    try:
        if int(i[0][-2:]) < 20:
            reader_updated.remove(i)
    except:
        pass

with open("csv_file.csv", 'w', newline='') as csv_file:
    write_to_file = csv.writer(csv_file, delimiter="|")
    write_to_file.writerows(reader_updated)

with open('csv_file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
