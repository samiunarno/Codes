s = []

def push():
    e = input("Enter the element")
    s.append(e)
    print(s)
def pop_el():
    if not s:
        print("Empty")
    else:
        e = s.pop()
        print("Removed",e)
        print(s)
while True : 
    print("Select The Operatiion 1 . Push 2. Pop")
    c = int(input("Enter the Choice : "))
    if c==1:
        push()
    elif c==2:
        pop_el() 
    elif c == 3:
        break
    else:
        print("Enter Correct Operation")                     