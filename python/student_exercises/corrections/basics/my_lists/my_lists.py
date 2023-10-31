def get_first_three_elements(lst):
    return lst[:3]

def get_last_two_elements(lst):
    return lst[-2:]

def reverse_list(lst):
    return lst[::-1]

def get_even_index_elements(lst):
    return [lst[i] for i in range(0,len(lst)) if i%2==0]
    return lst[::2]

def get_odd_index_elements(lst):
    return lst[1::2]

def remove_duplicates(lst):
    u = []
    [u.append(item) for item in lst if item not in u]
    return u

    return list(set(lst))

def square_elements(lst):
    return [x**2 for x in lst]

def double_elements(lst):
    return [x*2 for x in lst]

def sum_of_elements(lst):
    r = 0
    for i in lst:
        r += i
    return r
    return sum(lst)
def is_sorted(lst):
    #return lst.sort() == lst

    # for i in range(len(lst)-1):
    #     if lst[len(lst)-1-i] < lst[len(lst)-1-i-1]:
    #         return False
    # return True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

    

def count_occurrences(lst, element):
    c = 0
    for i in lst:
        if i == element:
            c+=1
    return c
    return lst.count(element)

def find_maximum(lst):
    if len(lst) == 0:
        return None
    
    max = lst[0]
    j = 1
    while j < len(lst):
        if max < lst[j]:
            max = lst[j]
        j+=1
    return max
    return max(lst)

def find_minimum(lst):
    if len(lst) == 0:
        return None
    
    min = lst[0]
    j = 1
    while j < len(lst):
        if min > lst[j]:
            min = lst[j]
        j+=1
    return min
    return min(lst)

def combine_lists(lst1: list, lst2):
    r = []
    for i in range(len(lst1)):
        r.append(lst1[i])
        r.append(lst2[i])
    return r

def is_palindrome(lst):
    return lst == lst[::-1]
