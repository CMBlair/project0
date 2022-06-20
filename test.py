import csv, pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='students')
class Student:
    def __init__(self, nameFirst, nameLast):
        self.nameFirst = nameFirst
        self.nameLast = nameLast
    def createStudent(
