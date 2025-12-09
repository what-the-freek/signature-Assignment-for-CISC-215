with open("golf.txt","a") as f:
    x = int(input("Please enter number of players"))
    for i in range(x):
        name = input("please enter Players Name")
        score = input("Please enter players score")
        f.write(f"Player Name: {name}  Score: {score}\n")