# Student 1 = Chukwuemeka Martins Ejike, Student ID = 20352671
# Student 2 = Mohhamed Aloba, Student ID = 20422224

# We imported random library to generate random number generator although we could've another library but it would've took longer
import random

# Created a class University, A name such as DCU = "self.name = name", A dictionary of courses and fees = "coursesNfees", An empty list to keep the student objects later = "self.students = []"
class University:
    def __init__(self, name, coursesNfees):
        self.name = name
        self.coursesNfees = coursesNfees
        self.students = []

#Part 1c "Takes an instance/object of class Student as input, generates a random 8 digit student ID and adds it to the student object as an attribute"
    def admit(self, Student): # Takes instance of student as input
        minimum = pow(10, 8-1) # Used pow method which forms it in powers to generate the student id easier
        maximum = pow(10, 8) - 1
        randNumber = random.randint(minimum, maximum)
       # Student.studentID = randNumber
        setattr(Student, 'studentID', randNumber)
        self.students.append(Student) # to admit the new student to the university

#Part 2 "Returns the first name, family name and ID of the students that are admitted to a university."
    def get_student(self):
        for obj in self.students:
            print(obj.fName+" "+ obj.lName + " " + str(obj.studentID))

# "A class called Student containing the following attributes Fname, Lname"
class Student:
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

#Part 3 "Return <fname>.<lname>@dcu.ie"
    def get_email(self):
        return self.fName+"."+self.lName+"@dcu.ie"

#Part 4 "Takes a list of courses chosen by the student and a university instance/object and returns the total fee."
    def calc_fees(self, list, University):
        courseList = University.coursesNfees.items() #Converted the dictionary into a list in University class to look for course and fees
        total = 0

        for course, fee in courseList:
            for lcourse in list:    #list course
                if lcourse == course:
                    total += fee

        print("The total is: " + str(total))

#Part 5 "Takes a dictionary of courses and marks and returns the sum of the values. This method also adds gpa as an attribute to the object."
    def calc_gpa(self, courseNmarks):
        marks = courseNmarks.items()
        sum = 0
        for course, v in marks:
            sum += v

        setattr(Student, 'gpa', sum) # set the attribute at runtime

        print(sum)


if __name__ == '__main__': # Used __name__ = __main__ so code can be executed in groups more orgnaised rather than just starting from the top

    DCU = University('DCU', {'Programming': 2000, 'Chemistry':1000, 'Finance': 2500, 'Math':600, 'Physics':1500})

    tom = Student('Tom', 'Hanks')
    johnny = Student('Johnny', 'Depp')
    anthony = Student('Anthony', 'Rogers')


    DCU.admit(tom)
    DCU.admit(johnny)
    DCU.admit(anthony)

    DCU.get_student()

    johnny.calc_fees(['Programming', 'Chemistry'], DCU)
    tom.calc_gpa({'Programming': 61, 'Chemistry': 39})

    print(getattr(tom, 'gpa'))

    #print(Anthony.get_email())

    #DCU.get_student()
