def selection_sort(lst):
    """"
    Sorts a list of integers using the selection sort algorithm
    Args: lst: list of integers to sort
    Returns: a new sorted list from least to greatest
    """
    for i in range(len(lst)):
        min_index = i # <-- Find first minimum index
        
        # start at the next number, for the entire length of list
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]: # if left index is smaller than right index set value to it
                min_index = j
            
        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index] # <-- swap the two indexes
    
    return lst

# --> Example Usage <--
print(selection_sort([33, 1, 89, 2, 67, 245]))
print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))