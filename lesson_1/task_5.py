import itertools as it

def count_find_num(primesL, limit):
    list_of_degree = list()
    list_of_numbers = list()
    #if limit <= 1000:
    for i in range(1, 11):
        list_of_degree.append(i)
        
    count_of_opt = it.product(list_of_degree, repeat=len(primesL))
    temp = 1
    for value in count_of_opt:
        for i in range(len(value)):
            temp *= (primesL[i] ** value[i])
        list_of_numbers.append(temp)
        temp = 1
    
    list_of_numbers = sorted(list_of_numbers)
    
    for value in list_of_numbers:
        if value > limit:
            list_of_numbers = list_of_numbers[:list_of_numbers.index(value)]
            break
    if list_of_numbers:
        pass
    else:
        return []   
    return [len(list_of_numbers), list_of_numbers[-1]]
   
    
primesL = [2, 5, 7]
limit = 500
assert count_find_num(primesL, limit) == [5, 490]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
