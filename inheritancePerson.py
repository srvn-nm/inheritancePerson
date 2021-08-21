class Person:
    def __init__(self,firstName,lastName,age,sexuality):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.sexuality = sexuality
    def printPerson(self):
        if self.sexuality == 'w' or self.sexuality == 'W':
            return(f"There is a beautiful woman named {self.firstName} {self.lastName} who is {self.age} year's old. ^-^")
        else:
            return(f"There is a handsome man named {self.firstName} {self.lastName} who is {self.age} year's old. ^-^")
class Student(Person):
    def __init__(self, firstName, lastName, age, sexuality, studentID, studentAverage):
        super().__init__(firstName, lastName, age, sexuality)
        self.studentID = studentID
        self.studentAverage = studentAverage
    def printPerson(self):
        return super().printPerson() + ' with student ID: ' + self.studentID + ' and this is the students average: ' + self.studentAverage
s1 = Student(input('enter your name here: '),input('enter you lastname here: '),input('enter your age here: '),input('enter w if you are woman and enter m if you are man: '),input('enter your student ID here: '),input('enter your average here: '))
print(s1.printPerson())