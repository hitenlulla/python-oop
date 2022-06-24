import datetime

class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self. pay = pay
        Employee.num_of_employees += 1

    # Normal method :: Takes self (instance) as the first parameter
    def print_full_name(self):
        return "{} {}".format(self.first, self.last)

    # Class method used to modify class variables :: Takes cls (class) as the first parameter
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Class methods can also be used as alternate constructors (Constructor overloading)
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Static method: Do not take any special arg as parameter as they are not reqd in logic
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

emp1 = Employee("Hiten", "Lulla", "100")
emp2 = Employee("Test", "User", "100")

# Calling a class method 
Employee.set_raise_amount(1.06)
print(Employee.raise_amount)

# Calling alternate constructor as class mehtod
emp1_str = "Meet-Lulla-10000"
emp3 = Employee.from_string(emp1_str)
print(emp3.__dict__)

# Calling static method
mydate = datetime.date(2016, 7, 10)
print(Employee.is_work_day(mydate))