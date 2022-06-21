
import pymysql
import csv
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='course_search', 
                             charset='utf8mb4')
cursor = connection.cursor()


class Student():
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
                                sql = 'DELETE FROM student WHERE lower(name) = %s'
                                cursor.execute(sql, (studentID))
                                connection.commit()
                                print(f"student {studentID} has been deleted.")
                except pymysql.Error as e:
                        print(f"There was an error deleting the student {e}")
    def importStudents(fileName):
        csv_data = csv.reader(open(fileName))
        for row in csv_data:
            cursor.execute('INSERT INTO student(name,major) VALUES(%s, %s)', row)
        connection.commit()
        print("Students Imported into Database")
Student.createStudent("Johnny", 12)
Student.importStudents("studentsList.csv")
