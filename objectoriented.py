class Employee:
    num_of_employee = 0
    payhike = 1.05
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employee +=1

    # def full_name(self):
    #     return('{} {}'.format(self.first, self.last))
    def increase_pay(self):
        self.pay = self.pay * self.payhike
    @classmethod
    def change_pay(cls, amount):
        cls.payhike = amount

    @classmethod
    def From_str(cls, str):
        first, last, pay = str.split(';')
        return cls(first, last, pay)

    @staticmethod
    def isworkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    @property
    def getemail(self):
        print("{}.{}@gmail.com".format(self.first,self.last))

    @property
    def full_name(self):
        return('{} {}'.format(self.first, self.last))

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(' ')

    @full_name.deleter
    def full_name(self):
        self.first = None
        self.last = None

    def __len__(self):
        return(len(self.full_name()))

    def __add__(self, other):
        return(self.pay + other.pay)


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    pass

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = []
    def add_emp(self, emp):
        self.employees.append(emp)

    def rem_emp(self, emp):
        self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("--->", emp.full_name)

emp1 = Employee('sukruth', 'ananth', 50000)

emp2 = Employee('ramesh', 'naidu', 70000)

empstr = 'lokesh;naidu;80000'

emp3 = Employee.From_str(empstr)


dev1 = Developer('ram', 'setu', 100000, "python")

mgr1 = Manager('sri', 'krishna', 120000)

print(mgr1.payhike)

mgr1.add_emp(emp3)
mgr1.add_emp(dev1)
mgr1.print_emp()

#print(dev1.prog_lang)

#print(Developer.__dict__(dev1))


#print(emp3.full_name())

#print(emp3.num_of_employee)


# emp2.increase_pay()
# print(emp2.pay)
#
# emp2.pay = 70000
emp2.change_pay(1.06)
# emp2.increase_pay()

#print(emp2.payhike)
# print(emp2.pay)

import datetime

date_time = datetime.date(2021, 6, 27)

# print(Employee.isworkday(date_time))



#Dunder for length
#
# print(len(emp1))
#
# print(emp1 + emp2)

print(emp1.full_name)

emp1.full_name = "arvind krishna"

print(emp1.full_name)

del emp1.full_name

print(emp1.full_name)