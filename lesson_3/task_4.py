import time
def dec_for_repeat_of_func(call_count, start_sleep_time, factor, border_sleep_time):
    def for_repeat_func(func):
        def wrapper():
            t = start_sleep_time
            counter = 1
            temp = start_sleep_time
            while t <= border_sleep_time:
                print(f"Запуск номер {counter}. Ожидание: {t} секунд.") 
                time.sleep(t)
                print(f"Результат декорируемой функций = {func()}.")
                counter += 1
                t = temp * 2 ** factor
                temp = t
                  
        return wrapper
    return for_repeat_func

@dec_for_repeat_of_func(4, 2, 1, 16)
def main():
    return "HELLO WORLD!"
    
main()