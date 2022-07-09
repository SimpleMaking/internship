class CyclicIterator:  
    def __init__(self, iter_obj) -> None:
        self.obj = iter_obj
        self.iter_obj = iter(iter_obj)
       
    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        while True:
            while self.counter < len(self.obj):
                result = next(self.iter_obj)
                self.counter += 1
                return result
            self.counter = 0
            self.iter_obj = iter(self.obj)
       
               
cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
