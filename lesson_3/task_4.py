import time
def dec_for_repeat_of_func(call_count, start_sleep_time, factor, border_sleep_time):
    def for_repeat_func(func):
        def wrapper():
            t = start_sleep_time
            counter = 1
            while counter <= call_count:
                print(f"Запуск номер {counter}. Ожидание: {t} секунд.") 
                time.sleep(t)
                print(f"Результат декорируемой функций = {func()}.")
                counter += 1
                if t < border_sleep_time:
                    t = (start_sleep_time * factor) ** counter
                else:
                    t = border_sleep_time
                  
        return wrapper
    return for_repeat_func

@dec_for_repeat_of_func(4, 1, 2, 8)
def main():
    return "HELLO WORLD!"
    
main()