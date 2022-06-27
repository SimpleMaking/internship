import itertools as it

CONST_LEN = 6
CONST_STR = 'banana'
def bananas(s) -> set:
    result = set()
    count_of_opt = it.combinations(range(len(s)), len(s) - CONST_LEN)
    cur_str = list(s)
    for value in count_of_opt:
        for value_ in value:
            cur_str[value_] = '-'
        cur_str = ''.join(cur_str)
        if cur_str.replace('-', '') == CONST_STR:
            result.add(cur_str)
        cur_str = list(s)
    return result

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}

assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

