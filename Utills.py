class Utils:
    basic_salary = 5000
    dictionary = {'s', 5000, 'm', 6000, 'p', 4000, 'e', 2000}

    def calculateExpectedSalary(self, experience, type):
        if experience >= 15:
            return self.basic_salary + (self.basic_salary * self.dictionary[type]) / 100
        elif 10 <= experience < 15:
            return self.basic_salary + (self.basic_salary * self.dictionary[type]) / 100
        elif 5 <= experience < 10:
            return self.basic_salary + (self.basic_salary * self.dictionary[type]) / 100
        else:
            return self.basic_salary
