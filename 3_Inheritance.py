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

# Developer is subclass to Employee
class Devleper(Employee):
    raise_amount = 1.10

    # Init method
    def __init__(self, first, last, pay, prog_lang):
        # Call init method of parent class
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev1 = Devleper("Hiten", "Lulla", "100000", "Python")
dev2 = Devleper("Meet", "Lulla", "200000", "Java")

print(Employee.raise_amount)
print(Devleper.raise_amount)

# Object of subclass can call methods of super class
print(dev1.print_full_name())

# Print the control flow
# print(help(Devleper))

# isinstance() - check if object is instance of a class
# issubclass() - check if class is subclass of another class
