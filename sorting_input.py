
def swap(input_arr, x, y):
    """
    Swaps two elements of array given the array and indexes of elements
    """
    input_arr[x], input_arr[y] = input_arr[y], input_arr[x]

def shift_down_in_heap(input_arr, start_index, end_index):
    """
    This method repairs the input array so that it can become a max heap
    @param input_arr: Input list of values
    @param start_index: Root index of tree/subtree
    @param end_index: End index of tree/subtree
    
    Returns: None 
    """
    root_index_subtree = start_index
    while (root_index_subtree * 2 + 1 <= end_index):
        child_index = root_index_subtree * 2 + 1
        swap_index = root_index_subtree
        if(input_arr[swap_index] < input_arr[child_index]):
            swap_index = child_index
        if child_index + 1 <= end_index and input_arr[swap_index] < input_arr[child_index + 1]:
            swap_index = child_index + 1
        if swap_index == root_index_subtree:
            return
        else:
            swap(input_arr, root_index_subtree, swap_index)
            root_index_subtree = swap_index
            
            
def heapify_array(input_arr):
    """
    Creates the max heap out of given list of values with the help of shift_down_in_heap function
    
    @param input_arr: List of input numbers to be sorted 
    
    Returns: None. Updates the array in place.  
    """
    input_len = len(input_arr)
    
    # Calculating floor((input_len - 2)/2)
    # As shifting down is needed only for non leaf elements
    start_index = (input_len - 2)//2
    
    while start_index >= 0 :
        shift_down_in_heap(input_arr, start_index, input_len-1)
        start_index = start_index - 1
    
def heap_sort(input_arr):
    """
    This function is to sort a list/tuple containing int values using  heap sort algorithm
    
    @param input_arr: list/tuple of integers 
    Returns: Sorted list of values in ascending order
    """
    input_len = len(input_arr)
    
    # No need to do anything if list is empty or has 1 element
    if not input_arr or input_len ==  1:
        return input_arr 
    
    # Handling the case where supplied input is a constant tuple (i. e. tuple)
    if isinstance(input_arr, tuple):
        input_arr = list(input_arr)

    # Creating MAX heap out of input supplied
    heapify_array(input_arr)
    
    end_index = len(input_arr) - 1
    while end_index > 0:
        # Swapping root(max element to end index of unsorted sub array)
        swap(input_arr, 0, end_index)
        
        # Updating unsorted sub array
        end_index = end_index - 1
        
        # Repairing the heap of unsorted sub array
        shift_down_in_heap(input_arr, 0, end_index)        
    return input_arr
   
   
   
if __name__ == '__main__':
     
    print heap_sort([])
    print heap_sort([5])
    print heap_sort([10, 9])
    print heap_sort ((5, 3, 2, 4, 6))
    print heap_sort(range(10, -11, -1))
    
    
    
    
    
    