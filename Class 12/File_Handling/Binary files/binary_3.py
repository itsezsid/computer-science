import pickle


def make_data():
    global lst
    file = open("static/binary3.dat", 'wb')
    s = int(input("enter the no. of dicitonaries: "))
    lst = []
    for i in range(s):
        d = {}
        n = int(input("enter the no. of records: "))
        for j in range(n):
            x = input("enter the details: ")
            y = int(input("enter a choice (1-int,2-str): "))
            if y == 1:
                g = int(input("enter the number: "))
                d[x] = g
            else:
                h = input("enter the word: ")
                d[x] = h
        k = input("do you want to enter more data?(y/n): ")
        if k in ['y', 'y']:
            op = 1
        else:
            op = 0
        if op == 1:
            s = open('static/binary3.dat', 'ab')
            x = int(input("enter the no. of additions: "))
            for i in range(x):
                a = input("enter the details: ")
                y = int(input("enter a choice (1-int,2-str): "))
                if y == 1:
                    x = int(input("enter the number: "))
                    d[a] = x
                else:
                    y = input("enter the word: ")
                    d[a] = y
            s.close()
        lst.append(d)
    pickle.dump(lst, file)
    file.close()
    file = open('static/binary3.dat', 'rb')
    print("the record is: ", pickle.load(file))
    file.close()


make_data()


def get_data():
    file = open("static/binary3.dat", 'rb')
    a = pickle.load(file)
    final = False
    fir = int(input("enter the number: "))
    for i in a:
        for key, value in i.items():
            if value == fir:
                print("the corresponding record of the fir no. ", value, ' is: ', i)
                final = True
                break
    if final == False:
        print("no such record !!!")
    file.close()


get_data()


def update_data():
    file = open("static/binary3.dat", 'rb')
    s = pickle.load(file)
    lst2 = []
    for i in s:
        if i['year'] < 2005:
            s = open("binary3.dat", 'wb')
            i['status'] = 'disposed'
            lst2.append(i)
    pickle.dump(lst2, s)
    s.close()
    file.close()
    file = open("static/binary3.dat", 'rb')
    print("the edited record is: ", pickle.load(file))
    file.close()


update_data()
