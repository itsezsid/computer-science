# Q1
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
        print(stack[top], 'is the top of stack')
        if len(stack) == 1:
            print("it is the only element")
        else:
            for a in range(top-1, -1, -1):
                print(stack[a])


def push(stack):
    l = int(len(stack))+1
    name = input("enter employee name: ")
    kr = [l, name]
    stack.append(kr)


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


