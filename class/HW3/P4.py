x = input()
check1 = False
check2 = False
check3 = False
check4 = False
check = 0
special = ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","[","]","{","}","?"]
if len(x) >= 8:
    check = check+1
for i in x:
    if i in special:
        check = check +1
        break
for a in x:
    if a .isupper:
        check=check+1
        break
for b in x:
    if b .isdigit:
        check=check+1
        break
if check<2:
    print("weak")
elif check==2:
    print("medium")
elif check==4:
    print("strong")
