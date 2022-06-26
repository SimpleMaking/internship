def count_find_num(primesL, limit):
    
    primesL = sorted(primesL)
    start_value = 1
    for value in primesL:
        start_value *= value
    if start_value > limit:
        return []
    general_numbers = [start_value]
    for i in primesL:
        for value in general_numbers:
            number = value * i
            if (number <= limit) and (number not in general_numbers):
                general_numbers.append(number)
                number *= i

    return [len(general_numbers), max(general_numbers)]
   
primesL = [2, 31, 67, 491]
limit = 951261292747
assert count_find_num(primesL, limit) ==  [100, 613440425482]

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

