import mysql.connector
from colorama import Fore, Style
from PyInquirer import prompt, print_json
import os
from pyfiglet import Figlet
from tabulate import tabulate


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


clear()
f = Figlet(font='slant', width=100)
print(Fore.MAGENTA + Style.BRIGHT +
      f.renderText('Lab Activity 4') + Style.RESET_ALL)


try:
    db = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        passwd="password",
        database="class12"

    )
    cursor = db.cursor()
except:
    print(Fore.RED + "Connection to Database failed" + Style.RESET_ALL)


def createTable():
    try:

        sql = 'create table Hospital (No int NOT NULL AUTO_INCREMENT PRIMARY KEY, Name varchar(20), Age int, Department varchar(30), Dateofadmin date, Charge int, GENDER varchar(3))'

        cursor.execute(sql)
        db.commit()
        print(Fore.GREEN + "Table hospital created successfully" + Style.RESET_ALL)

    except:
        print(Fore.RED + "Cannot create Table" + Style.RESET_ALL)


def insertData():
    try:
        sql = "INSERT INTO Hospital (Name , Age , Department , Dateofadmin , Charge , GENDER) VALUES (%s,%s,%s,%s,%s,%s)"
        values = [
            ('Arpit', 62, 'Surgery', '21/01/06', 300, 'M'),
            ('Zarina', 18, 'ENT', '12/12/05', 250, 'F'),
            ('Kareem', 22, 'Orthopedic', '19/02/19', 450, 'M'),
            ('Abhilash', 26, 'Surgery', '24/11/06', 300, 'M'),
            ('Dhanya', 24, 'ENT', '20/10/15', 350, 'F'),
            ('Siju', 23, 'Cardiology', '10/10/18', 800, 'M'),
            ('Ankita', 16, 'ENT', '13/04/06', 100, 'F'),
            ('Divya', 15, 'Cardiology', '10/11/12', 500, 'F'),
            ('Nidhin', 25, 'Orthopedic', '12/05/06', 700, 'M'),
            ('Hari', 28, 'Surgery', '19/03/17', 450, 'M')]
        cursor.executemany(sql, values)
        db.commit()
        print(Fore.GREEN + "Data inserted" + Style.RESET_ALL)
    except:
        print(Fore.RED + "Could not insert data" + Style.RESET_ALL)


def femalePatients():
    try:
        sql = 'SELECT Name FROM Hospital WHERE GENDER="F" and Department = "ENT"'
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        print(Fore.GREEN + "SQL execution successful" + Style.RESET_ALL)
    except:
        print(Fore.RED + "SQL execution Failed" + Style.RESET_ALL)


def doa():
    try:
        sql = 'select Name from Hospital order by Dateofadmin desc'
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        print(Fore.GREEN + "SQL execution successfull" + Style.RESET_ALL)
    except:
        print(Fore.RED + "SQL execution Failed" + Style.RESET_ALL)


def age20():
    try:
        sql = 'select count(name) from Hospital group by Department HAVING Age > 20'
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        print(Fore.GREEN + "SQL execution successful" + Style.RESET_ALL)
    except:
        print(Fore.RED + "SQL execution Failed" + Style.RESET_ALL)


def delCharge():
    try:
        sql = 'delete from Hospital where Age  > 60  OR Charge < 300'
        cursor.execute(sql)
        db.commit()
        print(Fore.GREEN + "SQL execution successful" + Style.RESET_ALL)
    except:
        print(Fore.RED + "SQL execution Failed" + Style.RESET_ALL)


def updatePediatric():
    try:
        sql = 'update Hospital set Department = "Pediatric" where Age < 16 '
        cursor.execute(sql)
        db.commit()
        print(Fore.GREEN + "SQL execution successful" + Style.RESET_ALL)
    except:
        print(Fore.RED + "SQL execution Failed" + Style.RESET_ALL)


def delName(name):
    try:
        sql = 'delete from Hospital where name = %s'
        val = (name, )
        cursor.execute(sql, val)
        db.commit()
        print(Fore.GREEN + "SQL execution successful" + Style.RESET_ALL)
    except:
        print(Fore.RED + "SQL execution Failed" + Style.RESET_ALL)


def updateDepartment(name, department):
    try:
        sql = 'update Hospital set Department = %s where Name = %s'
        val = (department, name, )
        cursor.execute(sql, val)
        db.commit()
        print(Fore.GREEN + "SQL execution successful" + Style.RESET_ALL)
    except:
        print(Fore.RED + "SQL execution Failed" + Style.RESET_ALL)


def newDate(date):
    try:
        sql = 'update Hospital set Dateofadmin = %s where year(Dateofadmin) = 2019'
        val = (date, )
        cursor.execute(sql, val)
        db.commit()
        print(Fore.GREEN + "SQL execution successful" + Style.RESET_ALL)
    except:
        print(Fore.RED + "SQL execution Failed" + Style.RESET_ALL)


def choiceForExec():
    questions = [

        {
            'type': 'list',
            'name': 'choiceForExec',
            'message': 'What would you like to do? ',
            'choices': ["Create Table", 'Insert Data', 'List all Female patients in ENT department', "List names of all patients with their date of admission in ascending order.", 'Count number of patients older than 20 [NOT WORKING]', 'Delete data of patients aged above 60 or those charged below 300', "Change the department of patients aged below 16 or below ,to Paediatric", "Accept a patient’s name and delete the record.", "Accept Department’s name and  Patients name. Change the respective records", "Replace all dates in the table with year 2006"]

        }

    ]
    answers = prompt(questions)
    if answers["choiceForExec"] == "Create Table":
        createTable()
    if answers["choiceForExec"] == 'Insert Data':
        insertData()
    if answers["choiceForExec"] == 'List all Female patients in ENT department':
        femalePatients()
    if answers["choiceForExec"] == 'List names of all patients with their date of admission in ascending order.':
        doa()
    if answers["choiceForExec"] == 'Count number of patients older than 20 [NOT WORKING]':
        age20()
    if answers["choiceForExec"] == 'Delete data of patients aged above 60 or those charged below 300':
        delCharge()
    if answers["choiceForExec"] == "Change the department of patients aged below 16 or below ,to Paediatric":
        updatePediatric()
    if answers["choiceForExec"] == "Accept a patient’s name and delete the record.":
        name = nameInput()
        delName(name["name"])
    if answers["choiceForExec"] == "Accept Department’s name and  Patients name. Change the respective records":
        name = nameInput()
        dept = deptInput()
        updateDepartment(name["name"], dept["dept"])
    if answers["choiceForExec"] == "Replace all dates in the table with year 2006":
        date = dateInput()
        newDate(date["date"])


def nameInput():
    questions = [

        {
            'type': 'input',
            'name': 'name',
            'message': 'Please the patient"s name : ',

        }

    ]

    answers = prompt(questions)
    return answers


def dateInput():
    questions = [

        {
            'type': 'input',
            'name': 'country',
            'message': 'Please enter the Date : ',

        }

    ]

    answers = prompt(questions)
    return answers


def deptInput():
    questions = [

        {
            'type': 'input',
            'name': 'dept',
            'message': 'Please enter the Department : ',

        }

    ]

    answers = prompt(questions)
    return answers


try:
    choiceForExec()
except:
    if KeyboardInterrupt:
        print(Fore.YELLOW + "Exitting Program" + Style.RESET_ALL)
    else:
        print(Fore.RED + "An error occured" + Style.RESET_ALL)
