x = input()
x = int(x)

if x>=18 and x<=99:
    print("eligible to vote")
elif x>=100:
    print("You are old. Congrats. you get a special lifetime voting honor")
else:
    print("ineligible to vote")