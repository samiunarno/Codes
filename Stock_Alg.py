st = [10,20,30,40]

print (st[0] + st[1])

sp = {
    'March 4' : 10,
    'March 5' : 20,
    'March 6' : 30,
}

print(sp['March 4'])

def get_squared_numbers(n):
    sn = []
    for i in n:
        sn.append(i*i)
    return sn 


n = [1,2,3,4,5]
get_squared_numbers(n)