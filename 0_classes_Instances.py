# Class is a blueprint
class Employee:
    # Constructor
    def __init__(self, first, last, pay):
        # Variables
        self.first = first
        self.last = last
        self. pay = pay


    # Method
    def print_full_name(self):
        return "{} {}".format(self.first, self.last)

    # Comparator
    def compare(self, other):
        if(self.pay == other.pay):
            return True
        else:
            return False

# Instance is actual object
emp1 = Employee("Hiten", "Lulla", "100")
emp2 = Employee("Test", "User", "100")

# Calling method on objects
print(emp1.print_full_name())
print(emp2.print_full_name())

if(emp1.compare(emp2)):
    print("Same salary")
else:
    print("Diff Salary")

