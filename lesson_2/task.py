from cmath import sqrt
import itertools as it
#STATIONS = {1:[0,1], 2:[1,4], 3:[4,1], 4:[5,5], 5:[7,2]} словарь где ключ это индекс станции, а значение - координаты станции
#INDEXES_OF_STATIONS = [2, 3, 4, 5] список индексов станций не включая самую первую, то есть отчет ведется с двойки

def main(STATIONS, INDEXES_OF_STATIONS):
    
    # Формирование словаря со всеми возможными расстояниями $
    count_of_opt = list(it.permutations(INDEXES_OF_STATIONS, len(STATIONS) - 1))
    dict_of_distances = dict()
    list_of_subtotals = list()
    value = 0; flag = True
    
    for i in range(len(count_of_opt)):
        for j in range(len(INDEXES_OF_STATIONS)):
                if flag:
                    value += sqrt(((STATIONS[1][0] - STATIONS[count_of_opt[i][j]][0]) ** 2) + ((STATIONS[1][1] - STATIONS[count_of_opt[i][j]][1]) ** 2)).real
                    flag = False
                else:
                    value += sqrt(((STATIONS[count_of_opt[i][j]][0] - STATIONS[count_of_opt[i][j - 1]][0]) ** 2) + ((STATIONS[count_of_opt[i][j]][1] - STATIONS[count_of_opt[i][j - 1]][1]) ** 2)).real
                    
        value += sqrt(((STATIONS[1][0] - STATIONS[count_of_opt[i][len(INDEXES_OF_STATIONS) - 1]][0]) ** 2) + ((STATIONS[1][1] - STATIONS[count_of_opt[i][len(INDEXES_OF_STATIONS) - 1]][1]) ** 2)).real
        dict_of_distances[i] = value
        flag = True
        value = 0
    # $ 
        
        
        
    # сортировка словаря, содержащего расстояния %
    sorted_dict_of_distances = dict()
    sorted_keys = sorted(dict_of_distances, key=dict_of_distances.get)  

    for key in sorted_keys:
        sorted_dict_of_distances[key] = dict_of_distances[key]
    # %
    
    
    
    # формирование вывода как в условии ^
    fin_str = ''
    itter = 0
    fin_str += str(tuple(STATIONS[1])) + '->'
    for value in count_of_opt[list(sorted_dict_of_distances.keys())[0]]:
        fin_str += str(tuple(STATIONS[value]))
        itter += 1
        if itter != len(count_of_opt) - 1:
            fin_str += '->'  
    fin_str += str(tuple(STATIONS[1])) + f'={sorted_dict_of_distances[list(sorted_dict_of_distances.keys())[0]]}'
    print(fin_str)
    # ^
    
main({1:[0,2], 2:[2,5], 3:[5,2], 4:[6,6], 5:[8,3]}, [2, 3, 4, 5])