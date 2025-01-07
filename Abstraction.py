class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluth = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started")

c1 = car()
c1.start()            