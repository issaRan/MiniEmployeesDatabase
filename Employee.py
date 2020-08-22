import ManageDb
from Utills import Utils


class Employee:
    def __init__(self):
        self._empName = input("Enter name :")
        self._empType = input("Enter type of the employee:")
        self._empEmail = input("Enter email of the employee")
        self._experience = int(input("enter experience"))
        self._mobile = input("Enter phone number")
        self._slaray = self.getSalary()

    def getSalary(self):
        return Utils().calculateExpectedSalary(self._empType, self._experience)
