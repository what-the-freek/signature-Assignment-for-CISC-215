x = input()
x = int(x)

if x<50:
    print("no discount. total price:", x)
elif x>=50 and x<100:
    print("5% Discount. discount:", x*.05, "total price:", x*.95)
else:
    print("10% Discount. discount:", x*.1, "total price", x*.9)