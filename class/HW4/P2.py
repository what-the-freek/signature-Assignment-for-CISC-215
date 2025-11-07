def Insure(x):
    return (x*.8)
if __name__ =="__main__":
    x = int(input("input cost to replace"))

    amount = Insure(x)
    print("you should insure for at least", amount)