def date():
    myfile = open(
        r'static/text1.txt', "r")
    text_str = myfile.read()
    text_initial = text_str.split()
    text = text_initial[::]
    a = []
    for i in range(0, 32):
        if i % 10 == 1 and i != 11:
            b = "st"
        elif i % 10 == 2 and i != 12:
            b = "nd"
        elif i % 10 == 3 and i != 13:
            b = "rd"
        else:
            b = "th"
        c = str(i)+b
        a.append(c)
    years = []
    for k in range(1600, 2101):
        str_years = str(k)+'.'
        years.append(str_years)
    months = ['', 'January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    months_sf = ['', 'Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.',
                 'Jun.', 'Jul.', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
    for i in text_initial:
        new_date = ''
        try:
            x = text.index(i)
            if i[2] == '/' and i[5] == "/":
                d = i[0:2]
                m = i[3:5] + "/"
                y = i[6:10] + "/"
                new_date = y+m+d+'.'
                text[x] = new_date

            if i in a and text_initial[x+2] in years:
                d = i[0:2]
                m_words = text[x+1]
                for j in range(len(months)):
                    if months[j] == m_words:
                        m = str(j)
                y = text[x+2][:4]
                new_date = y+'/'+m+'/'+d+'.'
                text.pop(x+2)
                text.pop(x+1)
                text[x] = new_date
                text.pop(x-1)

            if i in a:
                new_x = text.index(i)
                if text[new_x+3] in years:
                    if len(i) == 3:
                        d = i[:1]
                    else:
                        d = i[:2]
                    m_words = text[new_x+2]
                    for j in range(len(months_sf)):
                        if months_sf[j] == m_words:
                            m = str(j)
                    y = text[new_x+3][:4]
                    new_date = y+'/'+m+'/'+d+'.'
                    text.pop(new_x+3)
                    text.pop(new_x+2)
                    text.pop(new_x+1)
                    text[x] = new_date
        except:
            pass

    with open('text1.txt', 'w') as myfile_n:
        date_changed_text = ' '.join(text)
        myfile_n.write(date_changed_text)
        myfile_n.close()
        print(date_changed_text)

date()
