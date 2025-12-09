list1 = [5, 20, 15, 20, 25, 50, 20]  # given list of numbers

def remove_all_occurrences(list, value):  # Function to remove all occurrences of '20'
    while value in list:
        list.remove(value)
    print(list)

if __name__ == "__main__":
    remove_all_occurrences(list1, 20)