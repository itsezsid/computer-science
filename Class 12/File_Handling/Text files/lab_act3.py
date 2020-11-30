def names(name_list):
    with open('textfile3.txt', 'w') as myfile:
        myfile.writelines(name_list)
    myfile.close()
    print(name_list)
    menu()


def display_name(n):
    with open('textfile3.txt', 'r') as myfile:
        name_list = myfile.readlines()
        print(name_list[n-1])
        return namelist[n-1]


def display_s():
    with open('textfile3.txt', 'r') as myfile:
        name_list = myfile.readlines()
        for i in name_list:
            if i[0] in ["s", "S"]:
                print('the name/names that starts with an s is ', i)


def append_to_list(n):
    global namelist
    name_list = []
    for i in range(n):
        name_to_append = str(
            input("enter the name you want to append(add) to the list "))
        name_list.append(name_to_append)
        name_list.append('\n')
        namelist.append(name_to_append)
        namelist.append('\n')
    with open('textfile3.txt', 'a') as myfile:
        myfile.writelines(name_list)
    for i in range(0, len(namelist), 2):
        print(namelist[i])
    print('are the names in order ')


def menu():
    print("----------------------- menu to choose function ------------------------")
    print("enter your choice")
    print("enter 1 to display the nth name ")
    print("enter 2 to display names starting with s ")
    print("enter 3 to add/append more names ")
    print("if you want to execute all be my guest enter 4 ")
    x = int(input("enter choice "))
    try:
        if x == 1:
            index = int(input("enter the index to display name "))
            try:
                display_name(index)
            except:
                print("enter an index in range")
        if x == 2:
            display_s()
        if x == 3:
            number_of_names_to_append = int(
                input("enter how many names you want to add "))
            append_to_list(number_of_names_to_append)
        if x == 4:
            pass
    except:
        print("TRY AGAIN", "\n", "please enter a valid option")

    if x == 4:
        for i in range(1, 4):
            x = i
            if x == 1:
                index = int(input("enter the index to display name "))
                try:
                    display_name(index)
                except:
                    print("enter an index in range")
            if x == 2:
                display_s()
            if x == 3:
                number_of_names_to_append = int(
                    input("enter how many names you want to add "))
                append_to_list(number_of_names_to_append)


namelist = []
x = int(input("enter number of names to enter in list "))
for i in range(x):
    n = str(input("enter the list element "))
    namelist.append(n)
    namelist.append('\n')
names(namelist)
