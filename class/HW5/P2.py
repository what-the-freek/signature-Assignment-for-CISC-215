file = open("number_list.txt","w")
for i in range(1,101):
    x = 0+i
    file.write(f"{x}\n")
file.close