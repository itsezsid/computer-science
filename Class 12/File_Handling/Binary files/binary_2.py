import pickle


def make_data(op=0):
    global binfile
    if op == 0:
        binfile = open("static/binary2.dat", 'wb+')
    else:
        binfile = open("static/binary2.dat", 'ab+')
    n = int(input("enter number of records: "))
    print()
    for i in range(n):
        dict = {}
        cityname = input("enter city name: ")
        while 1:
            try:
                population = int(input("enter population of city"))
                if population < 0:
                    print("negative number detected. invalid input.")
                    continue
                break
            except:
                print("non-numeric input detected. please enter again.")
        while 1:
            try:
                hospitals = int(input("enter number of hospitals in city"))
                if hospitals < 0:
                    print("negative number detected. invalid input.")
                    continue
                break
            except:
                print("non-numeric input detected. please enter again.")
        while 1:
            try:
                schools = int(input("enter number of schools in city"))
                if schools < 0:
                    print("negative number detected. invalid input.")
                    continue
                break
            except:
                print("non-numeric input detected. please enter again.")
        while 1:
            try:
                density = int(input("enter city's population density: "))
                if density < 0:
                    print("negative number detected. invalid input.")
                    continue
                break
            except:
                print("non-numeric input detected. please enter again.")
        dict['city_name'] = cityname
        dict['population'] = population
        dict['hospitals'] = hospitals
        dict['school'] = schools
        dict['density'] = density
        pickle.dump(dict, binfile)
    print()


def get_data():
    cityname = input("enter cityname : ")
    global binfile
    binfile.seek(0)
    while 1:
        try:
            dict = pickle.load(binfile)
            if dict['city_name'] == cityname:
                print("record found. record is", dict)
                print()
                break
        except EOFError:
            print("record not found.")
            print()
            break


def update_data():
    dict_lst = []
    binfile.seek(0)
    while True:
        try:
            dict = pickle.load(binfile)
            dict_lst.append(dict)
        except EOFError:
            break
    binfile.seek(0)
    for dict in dict_lst:
        if dict['density'] in range(500, 1001):
            dict['city_name'] = "unknown"
        pickle.dump(dict, binfile)


def update_rec():
    cityname = input("enter city name of record to be modified: ")
    global binfile
    flag = False
    binfile.seek(0)
    while 1:
        try:
            dict = pickle.load(binfile)
            if dict['city_name'] == cityname:
                flag = True
                break
        except EOFError:
            print("no such record.")
            break
    if flag:
        field = input("enter field to be modified: ")
        if field in dict.keys():
            data = input("enter new value: ")
            dict_lst = []
            binfile.seek(0)
            while 1:
                try:
                    temp = pickle.load(binfile)
                    dict_lst.append(temp)
                except EOFError:
                    break
            binfile.seek(0)
            for i in range(len(dict_lst)):
                if dict_lst[i] == dict:
                    dict_lst[i][field] = data
                    for x in dict_lst:
                        pickle.dump(x, binfile)
                    break
                binfile.close()
        else:
            print("no such field in record.")


while 1:
    op = int(input("""what do you want to do?
0.create a new file
1.add data to existing file
input="""))
    if op in [0, 1]:
        break
    else:
        print("invalid input. accepted inputs are 0 and 1.")
make_data(op)
get_data()
update_data()
update_rec()
