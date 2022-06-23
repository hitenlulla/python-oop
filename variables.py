class Car:
    # Static variable
    wheels = 4

    # Instance variable
    def __init__(self, mil, com) -> None:
        self.mil = mil
        self.com = com

c1 = Car(10, "BMW")
c2 = Car(5, "Ferrari")

# Calling Instance variable
print(c1.mil)

# Calling Class Variable
print(Car.wheels)