


def counter_of_symbols(str: str):
    str = str.lower()
    dictionary = dict()
    counter = 0
    last_symb = None
    first = True
    for symbol in (list(str) + [None]):
        if first:
            dictionary[symbol] = 1
            first = False
            last_symb = symbol
        
        if last_symb and symbol != last_symb:
            
            dictionary[last_symb] = counter
            counter = 1
            last_symb = symbol

        else:  
          counter += 1  
    
    #sorting
    sorted_dictionary = dict()
    sorted_keys = sorted(dictionary, key=dictionary.get)  

    for key in sorted_keys:
        sorted_dictionary[key] = dictionary[key]
 
    return(list(sorted_dictionary.keys())[-1], sorted_dictionary[list(sorted_dictionary.keys())[-1]])

print(counter_of_symbols('aaaAAAbc'))