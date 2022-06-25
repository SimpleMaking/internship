from itertools import product

def count_find_num(primesL, limit):
    
    primesL = sorted(primesL)
    current_number = 1
    number_and_degree = list()
    number_and_degree_ = list()
    
    for i in range(len(primesL)):
        number_and_degree_.append(1)
        number_and_degree_.append(primesL[i])
        number_and_degree.append(number_and_degree_)
        number_and_degree_ = list()
        
    
    for i in range(len(primesL)):
        current_number *= primesL[i]


    value = 1
    count_of_numbers = 1
    itter = 0
    while current_number < limit:
        while True:
            for i in range(len(number_and_degree)):
                value *=  (number_and_degree[i][0] ** number_and_degree[i][1])
            if value > current_number:
                current_number = value
                value = 1       
                for i in range(len(number_and_degree)):
                    number_and_degree[i][1] = 1
                break
            else:
                number_and_degree[0][itter] += 1
                
    '''
    current_number = 1
    for i in range(len(primesL)):
        current_number *= primesL[i]
    start_value = current_number
    count_of_numbers = 1
    numbers_to_compare = list()
    while current_number < limit:
        while True:
            for i in range(len(primesL)):
                numbers_to_compare.append(start_value * primesL[i])
            if min(numbers_to_compare) > current_number:
                current_number = min(numbers_to_compare)
                break
            else:
                start_value = min(numbers_to_compare)
        print(numbers_to_compare)
        #current_number = min(numbers_to_compare)
        count_of_numbers += 1
        numbers_to_compare = list()
        ''' 
    return [count_of_numbers, current_number]


primesL = [2, 5, 7]
limit = 500
assert count_find_num(primesL, limit) == [5, 490]


