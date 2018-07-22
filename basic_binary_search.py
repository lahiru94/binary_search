import random
import numpy as np

def binary_search(arr, begin, end, val):
    if(end<begin):
        return False
    else:
        middle = begin + ((end - begin)/2)
        if(arr[middle] == val):
            return middle
        elif(arr[middle]<val):
            begin = middle+1
            return binary_search(arr, begin, end, val)
        else:
            end = middle-1
            return binary_search(arr, begin, end, val)

def random_binary_search(arr, begin, end, val):
    if(end<begin):
        return False
    else:
        middle = random.randint(begin, end) 
        if(arr[middle] == val):
            return middle
        elif(arr[middle]<val):
            begin = middle+1
            return binary_search(arr, begin, end, val)
        else:
            end = middle-1
            return binary_search(arr, begin, end, val)

def create_sorted_list(size):
    sorted_list = [] #list to keep the values in sorted order
    sorted_set = set() #set is maintained for faster lookup
    curr_rand = 0
    while(len(sorted_list)<size):
        curr_rand += 1
        if(bool(random.getrandbits(1))):
            sorted_list.append(curr_rand)
            sorted_set.add(curr_rand)
    return (sorted_list,sorted_set)
 
def create_search_items(sorted_set,max_val):

    '''
    Return random list of integers of type np.int(np int is similar to primitive type int)
    from the “discrete uniform” distribution in the closed interval [0, max_value].
    list will contain 300 items not available in sorted_set and 700 items available in 
    sorted_set
    '''
    present_values = [] #required size = 700
    absent_values = [] #required size = 300
    while (len(present_values)<700):
        temp = np.random.random_integers(low=0,high=max_val,size=None)
        if(temp in sorted_set):
            present_values.append(temp)
    while(len(absent_values)<300):
        temp = np.random.random_integers(low=0,high=max_val,size=None)
        if(temp not in sorted_set):
            absent_values.append(temp)
    return present_values + absent_values


if __name__ == "__main__":
    test_array = [1,3,4,6,7,8,13,450]
    # print random_binary_search(test_array,0,len(test_array)-1,13)
    sorted_list, sorted_set = create_sorted_list(int(10e5))
    search_items = create_search_items(sorted_set,sorted_list[-1])



