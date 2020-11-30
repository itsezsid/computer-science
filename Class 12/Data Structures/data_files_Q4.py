# Q2
def is_Empty(queue):
    if queue == []:
        return True
    else:
        return False


def enqueue(queue):
    if len(queue) == 0:
        rear = 0
    else:
        rear = len(queue)-1
    while True:
        court_name = str(input('enter court name :'))
        police_station_name = str(
            input('enter police station name where FIR is registered :'))
        fir = str(input('enter fir number :'))
        try:
            year = int(input('enter year of filing FIR :'))
        except:
            print('enter valid datatype (int) ')
        if len(queue) == 0 or year >= queue[rear][3]:
            break
        else:
            print('year entered lesser than last entry. Invalid Entry ')
    fir_tuple = (court_name, police_station_name, fir, year)
    queue.append(fir_tuple)
    if len(queue) == 1:
        front = rear = 0
    else:
        rear = len(queue)-1


def dequeue(queue):
    if is_Empty(queue):
        print("Underflow")
    else:
        item = queue.pop(0)
        print(item, 'is dequeued')
        if len(queue) == 0:
            front = rear = 0
        return item


def display(queue):
    if is_Empty(queue):
        print("queue is empty")
    elif len(queue) == 1:
        print(queue[0], '<==front,rear')
    else:
        front = 0
        rear = len(queue)-1
        print(queue[front], '<==front')
        for a in range(1, rear):
            print(queue[a])
        print(queue[rear], '<==rear')


queue = []

while True:
    print('---------------------------------------------QUEUE OPERATIONS-------------------------------------')
    print('1. ENQUEUE', '2. DEQUEUE', '3. DISPLAY', '4. EXIT', sep='\n')
    try:
        choice = int(input("make your choice :"))
    except:
        print('enter valid data type ')
        continue
    if choice == 1:
        enqueue(queue)
    elif choice == 2:
        dequeue(queue)
    elif choice == 3:
        display(queue)
    elif choice == 4:
        print("program terminated ")
        break
    else:
        print("Wrong input, enter a number from 1-4 ")
        print()
