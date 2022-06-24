class Figure:
    num_of_employees = 0

    def __init__(self, isCircle = False, length = None, width = None):
        self.length = length
        self.width = width
        self.isCircle = isCircle

    # Method overloading - One method can take multiple number of params and func acc.
    def calculate_area(self):
        if(not self.isCircle):
            if(self.width is None): 
                return self.length ** 2
            else:
                return self.length * self.width
        else:
            return 3.1415 * (self.length ** 2)

    # Method overriding - override the already written method of superclass
    def __repr__(self):
        return "Figure({},{},{})".format(self.isCircle, self.length, self.width)


circ = Figure(True, 10)
sqr = Figure(False, 10)
rect = Figure(False, 10, 5)

print(circ.calculate_area())
print(sqr.calculate_area())
print(rect.calculate_area())

print(circ)
print(sqr)
print(rect)