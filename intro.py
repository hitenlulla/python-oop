class Computer:
    # Constructor
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    
    # Method
    def get_details(self):
        print(str(self.cpu) + " " + str(self.ram) + "GB")

    # Comparator
    def compare(self, other):
        if(self.ram == other.ram):
            return True
        else:
            return False

comp1 = Computer("i5", 8)
comp2 = Computer("Ryzen 3", 16)

comp1.get_details()
comp2.get_details()

if(comp1.compare(comp2)):
    print("Same RAM")
else:
    print("diff Ram")

