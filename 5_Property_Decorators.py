class Employee:
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self. pay = pay
        Employee.num_of_employees += 1

    # Used to make a methods behave like a property
    
    # getter property
    @property
    def email(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    #Setter property
    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(' ')

    #Deleter property
    @full_name.deleter
    def full_name(self):
        print("Deleting name")
        self.first = None
        self.last = None
        
emp1 = Employee("Hiten", "Lulla", 100000)

# Getters
print(emp1.email)
print(emp1.full_name)

#Setters
emp1.full_name = "Meet Lulla"
print(emp1.full_name)

#Deleters
del emp1.full_name
print(emp1.full_name)