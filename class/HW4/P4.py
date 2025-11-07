def Seat(a,b,c):
    print("C seats", c)
    print("B seats", b)
    print("A seats", a)
    print("Total income",(a*20)+(b*15)+(c*10))

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    Seat(a,b,c)