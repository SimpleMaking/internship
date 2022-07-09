def func_args_caching(func):
    dict_for_cashe = {}
    def wrapper(*args):
        if args not in dict_for_cashe:  
            dict_for_cashe[args] = func(*args)
        return dict_for_cashe
    return wrapper

@func_args_caching
def multiplier(number: int):
    return number * 2

print(multiplier(3))
print(multiplier(5))
print(multiplier(3))