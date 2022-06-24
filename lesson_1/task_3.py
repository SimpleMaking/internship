def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7

 
