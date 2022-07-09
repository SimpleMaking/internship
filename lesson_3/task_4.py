import time
def dec_for_repeat_of_func(*args):
    def for_repeat_func(func):
        def wrapper():
            t = args[1]
            counter = 1
            temp = args[1]
            while counter <= args[0]:
                print(f"Запуск номер {counter}. Ожидание: {t} секунд.") 
                time.sleep(t)
                print(f"Результат декорируемой функций = {func()}.")
                counter += 1
                t = temp * 2 ** args[2]
                temp = t
                  
        return wrapper
    return for_repeat_func

@dec_for_repeat_of_func(4, 2, 1, 16)
def main():
    return "HELLO WORLD!"
    
main()