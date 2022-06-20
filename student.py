
import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='course_search', 
                             charset='utf8mb4')
cursor = connection.cursor()


class Student():
    def createStudent(self, name, major):
        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO student (name, major) VALUES (%s, (SELECT ID FROM majors WHERE lower(Major_Name) = %s))'
                cursor.execute(sql, (name, major))
                connection.commit()
                print(f"student:>> {name} created")
        except pymysql.Error  as e:
            print(f"There was an error creating user: {e}")
   
Student.createStudent(Student, "Johnny", "veterinary science")
