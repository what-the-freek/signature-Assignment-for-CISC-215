list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]  # given list with duplicates

def remove_duplicates(lst):  # Function to remove duplicates from the list
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    print(unique_list)

if __name__ == "__main__":
    remove_duplicates(list_with_duplicates)