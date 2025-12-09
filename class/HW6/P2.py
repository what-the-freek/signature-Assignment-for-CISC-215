list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]  # given list with empty strings
def remove_empty_strings(a):  # Function to remove empty strings from the list
    for i in a:
        if i == "":
            a.remove(i)
    print(a)

if __name__ == "__main__":
    remove_empty_strings(list1)