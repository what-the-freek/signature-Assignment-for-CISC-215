x = input("enter the name of a file")
file = open(x, "r")
for i in range(5):
    line = file.readline()
    print(line.strip())
file.close