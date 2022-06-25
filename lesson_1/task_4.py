import itertools as it

def compress_improve(data, selectors):
    list_of_values = list()
    for d, s in zip(data, selectors):
        if s:
            list_of_values.append(d)
        else:
            list_of_values.append("-")      
    return list_of_values


def bananas(s) -> set:
    result = set()
    count_of_opt = list(it.product([1, 0], repeat = len(s)))
    count_of_itters = 0
    str_ = ''
    for value in count_of_opt:
        value_ = ''.join(compress_improve(s, value))
        
        for i in value_:
            if i != "-":
                str_ += i
        if str_ == "banana":
            result.add(value_)
            count_of_itters += 1
            
        str_ = ''
     
    return result

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
