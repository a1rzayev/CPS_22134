"""Декораторы"""

def checker(function): # Передаем нашу функцию в декоратор, чтобы охватывать его
    def wrapper(*args, **kwargs): # Передаем аргументы функции в наш декоратор
        # Проверяем через try правильно работает или нет
        try:
            result = function(*args, **kwargs) 
        except Exception as exc:
            print(f"Error in: {exc}")
        else:
            print(f"No problems. Result: {result}")
            return result     
    return wrapper # Возвращаем декоратор

@checker # Указываем декоратор на нашу функцию
def calculate(expression):
    return eval(expression)

# Всё ок 
calculate("2+2")

# Ошибка 
calculate("2/0")