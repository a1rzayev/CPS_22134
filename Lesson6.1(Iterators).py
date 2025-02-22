""" Итерация списка"""  

mylist = [1, 2, 3, 4, 5]
# Указываем итератор на наш список
iterator = iter(mylist)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Выведет ошибку StopIteration из-за окончания элементов в списке 
print(next(iterator))

# Указание next() через цикл for
for elem in iterator:
    print(elem)

# Пример с классом 
class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number
    
    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        self.i += 1
        if (self.i > self.max_number):
            raise StopIteration
        return self.i
    
counter = Counter(10)
for elem in counter:
    print(elem)


