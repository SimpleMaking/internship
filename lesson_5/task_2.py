def my_sqrt(value: int):
    
    sqrt_value = value**0.5
    
    if sqrt_value.is_integer():
        return sqrt_value
    else:
        return None

print(my_sqrt(250))