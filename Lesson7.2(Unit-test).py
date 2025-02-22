"""Юнит-тесты"""

import unittest

# Создаем функции
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if(b == 0):
        raise ZeroDivisionError("Нельзя делить на 0!")
    return (a / b)

# Создаем юниттест класс
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(5, 3), 4) # Неправильное выполнение
        self.assertEqual(subtract(0, 4), -4)    

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(3, 2), 1.5)

        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == "__main__":
    unittest.main()