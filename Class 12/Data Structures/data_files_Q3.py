# Q3
def is_Empty(stack):
    if stack == []:
        return True
    else:
        return False


def pop(stack):
    if is_Empty(stack):
        print("Underflow")
    else:
        item = stack.pop()
        print(item, 'is popped')
        if len(stack) == 0:
            top = None
        else:
            top = len(stack)-1
        return item


def display(stack):
    if is_Empty(stack):
        print("Stack is empty")
    else:
        top = len(stack)-1
        print(stack[top], 'is the top of queue')
        if len(stack) == 1:
            print("it is the only element")
        else:
            for a in range(top-1, -1, -1):
                print(stack[a])


def push(stack):
    area = str(input('enter name of area: '))
    try:
        print('enter pincode of', area, end=': ')
        pin = int(input())
    except:
        print('invalid entry')
    dictionary_area = {area: pin}
    stack.append(dictionary_area)


stk = []

while True:
    print('---------------------------------------------STACK OPERATIONS-------------------------------------')
    print('1. PUSH', '2. POP', '3. DISPLAY', '4. EXIT', sep='\n')
    try:
        choice = int(input("make your choice: "))
    except:
        print('enter valid data type ')
        continue
    if choice == 1:
        push(stk)
    elif choice == 2:
        pop(stk)
    elif choice == 3:
        display(stk)
    elif choice == 4:
        print("program terminated ")
        break
    else:
        print("Wrong input, enter a number from 1-4 ")
        print('\n')


# Sample list: [{‘Basavanagudi’: 560004},{ ‘Konanakunte’:560062}]
