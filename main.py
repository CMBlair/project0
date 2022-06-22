from menu import menus
from student import Student
key = '' #just initializing a variable here for the main logic loop
while(key != "F"):
    menus.welcomeMessage()
    key = input()
    key = key.upper()
    while(key != "Q" and key != "F"):
        menus.mainMenu()
        key = input()
        key = key.upper()
        print(key)
        if key == "A":
            menus.studentRegistrationMenu()
            student_name = input()
            student_major = input()
            Student.createStudent(student_name, student_major)
        elif key == "B":
            menus.studentImportMenu()
            name = input()
            Student.importStudents(name)
        elif key == "C":
            menus.studentUpdateMenu()
        elif key == "D":
            menus.showStudentInfo()
            Student.showStudentInformation(Student)
        elif key == "E":
            menus.studentDeleteMenu()
            name = input()
            Student.deleteStudent(name)    
print("Thank you for using the Student Registration System")