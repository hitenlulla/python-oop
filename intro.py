class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    
    def get_details(self):
        print(str(self.cpu) + " " + str(self.ram) + "GB")

comp1 = Computer("i5", 8)
comp2 = Computer("Ryzen 3", 16)

comp1.get_details()
comp2.get_details()

