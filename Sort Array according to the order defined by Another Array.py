def sort_array_by_order(array, order):
    # Create a dictionary to map the order of each element in the order array
    order_dict = {val: i for i, val in enumerate(order)}
    
    # Use the order_dict to sort the array based on the order array
    sorted_array = sorted(array, key=lambda x: order_dict.get(x, len(order)))
    
    return sorted_array

array = [3, 2, 4, 1, 5]
order = [1, 2, 3, 4, 5]

sorted_array = sort_array_by_order(array, order)

print(sorted_array)