def counter_of_symbols(str: str):
    str = str.lower()
    dictionary = dict()
  
    for symbol in str:
        dictionary[symbol] = dictionary.get(symbol, 0) + 1
     
    #sorting
    sorted_dictionary = dict()
    sorted_keys = sorted(dictionary, key=dictionary.get)  

    for key in sorted_keys:
        sorted_dictionary[key] = dictionary[key]
 
    return (list(sorted_dictionary.keys())[-1], sorted_dictionary[list(sorted_dictionary.keys())[-1]])

print(counter_of_symbols('CsCCCccccaaaaAAAbc'))