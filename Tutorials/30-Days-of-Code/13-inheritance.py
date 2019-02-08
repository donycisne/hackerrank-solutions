'''
  Task:
    You are given two classes, Person and Student,
    where Person is the base class and Student is the derived class.
    Completed code for Person and a declaration for Student
    are provided for you in the editor.
    Observe that Student inherits all the properties of Person.
    Complete the Student class by writing the following:
    - A Student class constructor, which has 4 parameters:
        1 - A string, firstName.
        2 - A string, lastName.
        3 - An integer, id.
        4 - An integer array (or vector) of test scores, scores.
    - A char calculate() method that calculates a Student object's average
    and returns the grade character representative of their calculated average:
      Grading Scale:
        Letter |    Average
      ---------| --------------
          O    | 90 <= a <= 100
          E    | 80 <= a < 90
          A    | 70 <= a < 80
          P    | 55 <= a < 70
          D    | 40 <= a < 55
          T    |    a < 40
'''

# Solution
class Person:
  def __init__(self, firstName, lastName, idNumber):
    self.firstName = firstName
    self.lastName = lastName
    self.idNumber = idNumber
  def printPerson(self):
    print("➡ Name:", self.lastName + ",", self.firstName)
    print("➡ ID:", self.idNumber)

class Student(Person):
  def __init__(self,firstName,lastName,idNum,scores):
    self.firstName=firstName
    self.lastName=lastName
    self.idNumber=idNum
    self.scores=scores

  def calculate(self):
    a=sum(self.scores)/len(self.scores)
    if a >= 90:
        return 'O'
    elif 90>a>=80:
        return 'E'
    elif 80>a>=70:
        return 'A'
    elif 70>a>=55:
        return 'P'
    elif 55>a>=40:
        return 'D'
    else:
        return 'T'

line = input('Enter [name] [last name] [7 digits]: ').split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input('Enter an ID number: ')) # not needed for Python
scores = list( map(int, input('Enter [score] [score]: ').split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("➡ Grade:", s.calculate())
