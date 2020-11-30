import pickle


def make_data(op=0):
    global binfile
    if op == 0:
        binfile = open("static/binary1.dat", 'wb+')
    else:
        binfile = open("static/binary1.dat", 'ab+')
    n = int(input("enter number of dictords: "))
    print()
    for i in range(n):
        dict = {}
        report_id = str(input("enter report id: "))
        date = str(input("enter date: "))
        airport = str(input("enter airport: "))
        aircraft_id = str(input("enter aircraft id: "))
        aircraft_type = str(input("enter aircraft type: "))
        pilot_total_hours = int(
            input("enter total hours flown by the pilot: "))
        midair = bool(input('is the flight in mid air? :'))

        dict['report_id'] = report_id
        dict['date'] = date
        dict['airport'] = airport
        dict['aircraft_id'] = aircraft_id
        dict['aircraft_type'] = aircraft_type
        dict['pilot_total_hours'] = pilot_total_hours
        dict['midair'] = midair
        pickle.dump(dict, binfile)
    print()


def get_data():
    aircraft_id = input("enter aircraft id: ")
    global binfile
    binfile.seek(0)
    while 1:
        try:
            dict = pickle.load(binfile)
            if dict['aircraft_id'] == aircraft_id:
                print("record found. record is", dict)
                print()
                break
        except EOFError:
            print("record not found.")
            print()
            break


def update_data():
    global binfile
    report_id = input("enter report_id to modify : ")
    binfile.seek(0)
    dict_list = []
    while 1:
        try:
            x = pickle.load(binfile)
            dict_list.append(x)
        except EOFError:
            break
    for i in range(len(dict_list)):
        a = 0
        if dict_list[i]['report_id'] == report_id:
            field = str(input('enter field to edit: '))
            dict_list[i][field] = input(
                'enter what you want to change value to: ')
    pickle.dump(dict_list, binfile)


make_data()
print('----------------------enter choice-------------------')
print("enter 1 to view data ")
print("enter 2 to update data ")
print("enter 3 to append data ")
c = int(input(''))
if c == 1:
    get_data()
if c == 2:
    update_data()
if c == 3:
    pass
