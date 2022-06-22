import pymysql
import csv
import re
from tabulate import tabulate
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='course_search', 
                             charset='utf8mb4')
cursor = connection.cursor()


class Student(object):
    def createStudent(name, major):
        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO student (name, major) VALUES (%s, %s)'
                cursor.execute(sql, (name, major))
                connection.commit()
                print(f"student:>> {name} created")
        except pymysql.Error  as e:
            print(f"There was an error creating user: {e}")
    def deleteStudent(studentID):
        try:
            with connection.cursor() as cursor:
                sql = 'DELETE FROM student WHERE id = %s'
                name = Student.getStudentName(studentID)
                cursor.execute(sql, (studentID))
                connection.commit()
                print(f"student {name} has been deleted.")
        except pymysql.Error as e:
                print(f"There was an error deleting the student {e}")
    def importStudents(fileName):
        csv_data = csv.reader(open(fileName))
        for row in csv_data:
            cursor.execute('INSERT INTO student(name,major) VALUES(%s, %s)', row)
        connection.commit()
        print("Students Imported into Database")
    def updateStudentInfo(self):
        try:
            with connection.cursor() as cursor:
                self.getAllStudentsAndMajors(self)
                name = input("Enter the ID of the student you want to update:  ")
                self.getAllMajors()
                major = input("Enter the new major ID (1-16):  ")
                sql = 'UPDATE student SET major = %s WHERE id = %s'
                cursor.execute(sql, (major, name))
                connection.commit()
                name = self.getStudentName(name)
                major = self.getStudentMajor(major)
                print(f"student {name}'s major  has been updated to {major}.")
        except pymysql.Error as e:
            print(f"There was an error updating the student {e}")
    def getAllStudentsAndMajors(self):
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT student.id, student.name, majors.Major_Name FROM student join majors on majors.ID = student.major'
                cursor.execute(sql)
                print("The current List of Students: ")
                myresult = cursor.fetchall()
                print(tabulate(myresult, headers=['ID', 'Name', 'Major']))
        except pymysql.Error as e:
            print(f'There was an error retrieving your request. {e}')
    def getAllStudents(self):
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT id, name FROM student'
                cursor.execute(sql)
                print("The current List of Students: ")
                myresult = cursor.fetchall()
                print(tabulate(myresult, headers=['ID', 'Name']))
        except pymysql.Error as e:
            print(f'There was an error retrieving your request. {e}')
    def getAllMajors():
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT ID, Major_Name FROM majors LIMIT 16'
                cursor.execute(sql)
                myresult = cursor.fetchall()
                print(tabulate(myresult, headers=['ID', 'Name']))
        except pymysql.Error as e:
            print(f'There was an error retrieving your request. {e}')
    def showStudentInformation(self):
        try:
            with connection.cursor() as cursor:
                self.getAllStudents(self)
                id = input("Enter the ID of the student you wish to know more about: ")
                sql = 'SELECT courses.Course_ID, courses.Course_Name FROM major_courses JOIN courses WHERE courses.Course_ID = major_courses.Course_ID AND major_courses.id = (SELECT major FROM student WHERE id = %s)'
                cursor.execute(sql, (id))
                myresult = cursor.fetchall()
                print("The courses that" + self.getStudentName(id) + "is required to take to graduate with a degree in" + self.getStudentMajor(id))
                print(tabulate(myresult, headers=['Course ID', 'Course Name']))
        except pymysql.Error as e:
            print(f'There was an error retrieving your request. {e}')
    def getStudentName(id):
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT name FROM student WHERE id = %s'
                cursor.execute(sql,(id))
                name = str(cursor.fetchone())
                name = re.sub(r"[^a-zA-Z0-9]+", ' ', name)
        except pymysql.Error as e:
            print(f'There was an error retrieving your request. {e}')
        return name
    def getStudentMajor(id):
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT majors.Major_Name FROM majors join student WHERE student.major = majors.ID AND  student.id = %s'
                cursor.execute(sql,(id))
                student_major = str(cursor.fetchone())
                student_major = re.sub(r"[^a-zA-Z0-9]+", ' ', student_major)
        except pymysql.Error as e:
            print(f'There was an error retrieving your request. {e}')
        return student_major
