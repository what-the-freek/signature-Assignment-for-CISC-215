n = 6

for i in range(1, n+1):
    if n>0 and n<5:
        continue
    print("#", end="")
    for j in range(2, i+1):
        print(end=" ")    
    print("#")