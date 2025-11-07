buy = 1000
price = 100*(buy)
pay = price*.03
sell = 1000
price2 = 142.75*(sell)
pay2 = price2*.03
total = price2 - (pay + pay2 + price)
print("Joe paid", price," dollars for the stock, and paid his broker", pay,". Joe sold his stock for", \
     price2, "and paid his broker,  again, for", pay2, "dollars. After paying his broker, joe made", total)
if total > 0:
    print("joe made money")
else:
    print("joe lost money")