



def get_highest(lst):
    # highest = lst[0]
    # for el in lst:
    #     if el > highest:
    #         highest = el
    # return highest 

    highest = lst[0]
    for i in range(1, len(lst)):
        el = lst[i]
        if el > highest:
            highest = el
    return highest

    # return max(lst)

def count_letter(lst, substring):
    # counter = 0
    # for string in lst:
    #     for letter in string:
    #         if letter == substring:
    #             counter += 1
    # return counter

    # counter = 0
    # for string in lst:
    #     counter += string.count(substring)
    # return counter

    return "".join(lst).count(substring)

def zip_lists(a, b):
    # result = []
    # for i in range(len(a)):
    #     el_a = a[i]
    #     el_b = b[i]
    #     result.append([el_a, el_b])
    # return result

    return zip(a, b)

def sum_lists(a, b):
    zipped = zip_lists(a, b)
    result = []
    for z in zipped:
        result.append(sum(z))
    return result

    # return [x + y for x, y in zip(a, b)]

if __name__ == '__main__':

    lst = [1, 2, 3, 4, 5, 6, 10000, 9]
    highest_value = get_highest(lst)
    print(highest_value) # 10000

    names = ['Conrad', 'Arnaud', 'Monica', 'Fabrice']
    count_o = count_letter(names, 'o')
    print(count_o) # 2

    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]

    zipped = zip_lists(a, b)
    print(zipped) # [[1, 6], [2, 7], [3, 8], [4, 9], [5, 10]]

    sum_two_lists = sum_lists(a, b)
    print(sum_two_lists) # [7, 9, 11, 13, 15]

    



