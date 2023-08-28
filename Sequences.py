def remove_duplicates_in_place(input_list):
    temporary_list = []
    
    for item in input_list:
        if item not in temporary_list:
            temporary_list.append(item)
    
    input_list.clear()
    input_list.extend(temporary_list)

# Test the function
my_list = [1, 2, 3, 1, 2, 4, 5, 4, 6, 2]
print("List Before:", my_list)

remove_duplicates_in_place(my_list)

print("List After:", my_list)
