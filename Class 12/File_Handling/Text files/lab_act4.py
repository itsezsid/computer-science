def rev_vowels(n):
    with open('Q4.txt', 'r') as myfile:
        data = []
        for i in range(n):
            a = myfile.readline()
            b = a.split()
            for i in range(len(b)):
                if b[i][0] in "aeiouAEIOU":
                    if i == 0:
                        c = b[i][::-1]
                    else:
                        c = ' '+b[i][::-1]
                    b[i] = c
            data.append(b)
            data.append('\n')
    with open('Q4.txt', 'w') as file:
        for i in range(len(data)):
            file.writelines(data[i])


x = int(input(('enter number of lines in Q4.py ')))
with open('Q4.txt', 'w') as myfile:
    for i in range(x):
        print('please enter text in the ', i+1, 'th line')
        text = str(input('')) + '\n'
        myfile.write(text)
    myfile.close()
rev_vowels(x)
