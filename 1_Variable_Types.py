class Employee:
    # Declaring Class variable
    num_of_employees = 0
    raise_amount = 1.04

    # Constructor
    def __init__(self, first, last, pay):
        # Instance variable
        self.first = first
        self.last = last
        self. pay = pay

        # Accessing Class variables
        Employee.num_of_employees += 1

emp1 = Employee("Hiten", "Lulla", "100")
emp2 = Employee("Test", "User", "100")

# Accessing instance variables
print(emp1.first)
print(emp2.last)

# Accessing class variables
print(Employee.num_of_employees)

