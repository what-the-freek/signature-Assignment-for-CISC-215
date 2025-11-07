# Midterm Coding Problem
def display_intro():
    print("This Program will calculate the total cost of three itesms based on the given prices and the number of items")
def calculate_total():
    t = 0
    for i in range(3):
        x = float(input("input price of item "))
        y = float(input("input quantity of item "))
        t = t+(x*y)
    print(f"Your grocery bill is: ${t:.2f}")


display_intro()
calculate_total()