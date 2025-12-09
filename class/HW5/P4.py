words = int(input("How many words would you like to write?"))
file = open("word.txt","a")
for i in range(1, words + 1):
    x = input(f"word {i}\n")
    file.write(x)
file.close