import csv
import random
# import pandas as pd


def read_csv() -> list:
    student = []
    with open('database.csv', 'r', encoding='utf-8-sig') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = row[0]
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["faculty"] = row[3]
            temp["cource"] = row[4]
            temp["grant"] = int(row[5])
            student.append(temp)
    return student
    #     df = pd.read_csv('database.csv', skiprows=1)
    #     for row in df:
    #         temp = {}
    #         temp["id"] = row[0]
    #         temp["last_name"] = row[1]
    #         temp["first_name"] = row[2]
    #         temp["faculty"] = row[3]
    #         temp["cource"] = row[4]
    #         temp["grant"] = int(row[5])
    #         student.append(temp)
    # return student


def find_stud(students):
    stud = input("Insert student's surname: ")
    # data = pd.read_csv('database.csv')
    # for line in data:
    #     if stud in line:
    #         print(line)
    for i in students:
        if i['last_name'] == stud:
            return i


def get_student():
    result = {}
    result["id"] = int(random.randint(10000, 99999))
    result["last_name"] = input('Insert surname: ')
    result["first_name"] = input('Insert first name: ')
    result["faculty"] = input('Insert faculty: ')
    result["cource"] = input('Insert cource: ')
    result["grant"] = input('Insert grant: ')
    return result


def stud_by_grant(students):
    result = []
    low = int(input('Insert low: '))
    high = int(input('Insert high: '))
    for i in students:
        if low <= i['grant'] <= high:
            result.append(i)
    return result


def show_base():
    data = pd.read_csv('database.csv')
    print(data.head())


def add_stud(students):
    print('Insert students data (Surname Name Faculty Course Money): ')
    student = get_student()
    students.append(student)


def del_stud(students):
    student = input("Insert student's surname: ")
    for i in students:
        if i['last_name'] == student:
            students.remove(i)


def upd_stud(students):
    student = input("Insert student's surname: ")
    for i in students:
        if i['last_name'] == student:
            i = input('Insert new data (Surname Name Faculty Course Money): ')


def exp_json():
    df = pd.read_csv('database.csv')
    df.to_json('database.json')


def exp_xlsx():
    df = pd.read_csv('database.csv')
    df.to_excel('database.xlsx', index=None, header=True)