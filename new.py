class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def welcome(self):
        print("Welcome to Portal")
    def names (self):
        print(self.name)        
    def get_marks(self):
        return self.marks    
    



s = student("Karan",90)
s.welcome()
print(s.names())
print(s.get_marks())
