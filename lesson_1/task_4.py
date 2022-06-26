import itertools as it

def compress_improve(data, selectors):
    list_of_values = list()
    for d, s in zip(data, selectors):
        if s:
            list_of_values.append(d)
        else:
            list_of_values.append("-")      
    return ''.join(list_of_values)


def bananas(s) -> set:
    result = set()
    count_of_opt = it.product([1, 0], repeat = len(s))
    for value in count_of_opt:
          
        value_ = compress_improve(s, value)
        if value_.replace("-", "") == "banana":
            result.add(value_)
    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}

assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

