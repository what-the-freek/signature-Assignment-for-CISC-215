my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6] # given list with mixed data types

def separate_data_types(list):  # Function to separate integers from the list
    integers = []
    for item in list:
        if isinstance(item, int):
            integers.append(item)
    print(integers)

if __name__ == "__main__":
    separate_data_types(my_list)