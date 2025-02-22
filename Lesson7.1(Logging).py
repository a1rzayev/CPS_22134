import logging

# Определяем базоваую конфигурацию для логирования 
logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

# Деление и проверка
def divide(a, b):
    logging.info(f" Выполняем деление: {a} / {b}")
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error("Ошибка: Деление на ноль!")
    else:
        logging.debug(f"Результат: {result}")
        return result
    
# Указываем начало программы через информирование
logging.info("Начало программы")

divide(10, 2)
divide(5, 0)

logging.warning("Это предупреждение")
logging.info("Конец программы")