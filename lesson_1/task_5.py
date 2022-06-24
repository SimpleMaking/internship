def count_find_num(primesL, limit):
    
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
         
    return [count_of_numbers, current_number]


primesL = [2, 5, 7]
limit = 500
assert count_find_num(primesL, limit) == [5, 490]


