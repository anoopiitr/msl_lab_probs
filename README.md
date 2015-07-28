PYTHON IMPLEMENTATION FOR SOME PROBLEMS

Problem 3: Python implementation of sorting algorithm(heap sort). Chose heap sort because of O(N ln N) complexity 
           even in worst case scenarios, which is better than other sorting techniques like quicksort(in worst case)
           
           Assumptions:
                User supplies list/tuple of integer values. In case of floats and doubles it may give incorrect result
                as issue with equality of floats/doubles is not handled for the time being.
          
           How to use the method :
                Need to import heap_sort from sorting_input module. Call it supplying a sequence of values.
                The method returns sorted array.

           Note :  
                It could have sorted the values in place. But to allow sorting of tuples as well it converts input
                to mutable sequence and returns the same after sorting.
                
