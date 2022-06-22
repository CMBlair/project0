from student import Student

myStudent = Student()

class menus():
    def welcomeMessage():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\033[1;32m Welcome to the Student Registration System \033[0;0m")

    def mainMenu():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Please enter one of the options below")
        print("A: Register a Student")
        print("B: Import a List of Students")
        print("C: Update an Existing Student")
        print("D: Remove a Student from the System")
        print("Q: Quit")
    
    def studentRegistrationMenu():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        Student.getAllMajors()
        print("Please enter the Name of the student, and then enter their major ID from the list above ")

    def studentImportMenu():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\033[2;31;43mThe import from list option only accepts .CSV files!\033[0;0m")
        print("Please enter the file name, with extension below.")
    
    def studentUpdateMenu():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        Student.updateStudentInfo(Student)
    
    def studentDeleteMenu():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        Student.getAllStudents(Student)
        print("Please enter the ID of the student you would like the remove from the system.")

