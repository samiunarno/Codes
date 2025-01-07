class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        s = 0 
        for i in self.marks :
            s +=i
        print(self.name,"Your Average is ",s/3)


s1 = student("Karan",[90,98,87])
s1.get_avg()   

# to change data
s1.name = "Arno"
s1.marks = [91,93,94]
s1.get_avg()
        