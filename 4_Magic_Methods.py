class Employee:
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self. pay = pay
        self.email = "{}.{}@gmail.com".format(self.first.lower(), self.last.lower())
        Employee.num_of_employees += 1

    def print_full_name(self):
        return "{} {}".format(self.first, self.last)

    # repr method is used to represent the instance to a developer
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    # str method is used to represent the instance to a user
    def __str__(self):
        return self.print_full_name() +  " - " + self.email

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.print_full_name())

dev1 = Employee("Hiten", "Lulla", 100000)
dev2 = Employee("Meet", "Lulla", 200000)

print(dev1)                         # __str__
print(repr(dev2))                   # __repr__

print(dev1 + dev2)                  # __add__
print(len(dev1))                    # __len__