try:
    x = input()
    file = open(x, "r")
    for i in range(5):
        line = file.readline()
        print(line.strip())
    file.close
except IOError:
    print("file does not exist")
except ValueError:
    print("ValueError caught") # I couldnt get a value error to come up