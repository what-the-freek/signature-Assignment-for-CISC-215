list_of_lists = [[1, 2], [3, 4], [5, 6, 7]] # given nested list

def flatten_list(nested_list):  # Function to flatten the nested list
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    print(flat_list)

if __name__ == "__main__":
    flatten_list(list_of_lists)