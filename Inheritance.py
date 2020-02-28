class Person(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
        # To check if this person is employee
    def isEmployee(self):
        return False
# Inherited or Sub class (Note Person in bracket)
class Employee(Person):
    def isEmployee(self):
        return True
emp = Person("Ravi")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Raju")  # An Object of Employee
print(emp.getName(), emp.isEmployee())