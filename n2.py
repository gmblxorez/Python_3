import math
from typing import List, Union

# Определяем тип для чисел
Num = Union[int, float]


class MathOperations:
    """Класс с математическими операциями"""

    @staticmethod
    def sum_two(a: Num, b: Num) -> Num:
        """Складывает два числа"""
        if not all(isinstance(x, (int, float)) for x in [a, b]):
            raise ValueError("Нужны числа!")
        return a + b

    @staticmethod
    def subtract(a: Num, b: Num) -> Num:
        """Вычитает второе число из первого"""
        MathOperations._check_numbers(a, b)
        return a - b

    @staticmethod
    def multiply(a: Num, b: Num) -> Num:
        """Умножает два числа"""
        MathOperations._check_numbers(a, b)
        return a * b

    @staticmethod
    def divide(a: Num, b: Num) -> Num:
        """Делит первое число на второе"""
        MathOperations._check_numbers(a, b)
        if b == 0:
            raise ZeroDivisionError("Нельзя делить на ноль!")
        return a / b

    @staticmethod
    def power(a: Num, b: Num) -> Num:
        """Возводит число в степень"""
        MathOperations._check_numbers(a, b)
        return a ** b

    @staticmethod
    def fact(n: int) -> int:
        """Вычисляет факториал"""
        if not isinstance(n, int):
            raise TypeError("Нужно целое число")
        if n < 0:
            raise ValueError("Факториал только для положительных")
        return math.factorial(n)

    @staticmethod
    def sin(x: Num) -> float:
        """Вычисляет синус угла"""
        MathOperations._check_numbers(x)
        return math.sin(x)

    @staticmethod
    def med(numbers: List[Num]) -> Num:
        """Находит медиану списка"""
        if not numbers:
            raise ValueError("Список пуст")
        MathOperations._check_numbers(*numbers)
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        mid = n // 2
        return sorted_nums[mid] if n % 2 else (sorted_nums[mid - 1] + sorted_nums[mid]) / 2

    @staticmethod
    def _check_numbers(*args: Num) -> None:
        """Проверяет, что все аргументы - числа"""
        for num in args:
            if not isinstance(num, (int, float)):
                raise TypeError("Все аргументы должны быть числами")


def show_menu():
    """Показывает меню операций"""
    print("\nДоступные операции:")
    ops = [
        "1. Сложение",
        "2. Вычитание",
        "3. Умножение",
        "4. Деление",
        "5. Степень",
        "6. Факториал",
        "7. Синус",
        "8. Медиана",
        "exit - Выход"
    ]
    print("\n".join(ops))
    print("-" * 20)


def get_num(prompt: str) -> Num:
    """Получает число от пользователя"""
    while True:
        try:
            val = input(prompt)
            return float(val) if "." in val else int(val)
        except ValueError:
            print("Ошибка! Введите число")


def get_nums(prompt: str) -> List[Num]:
    """Получает список чисел"""
    while True:
        try:
            vals = input(prompt).split()
            return [float(x) if "." in x else int(x) for x in vals]
        except ValueError:
            print("Ошибка! Вводите только числа через пробел")


def run_calculator():
    """Запускает калькулятор"""
    show_menu()

    while True:
        choice = input("\nВыберите операцию: ").strip().lower()

        if choice in ("exit", "quit", "q"):
            print("Работа завершена")
            break

        try:
            if choice == "1":
                a, b = get_num("Первое число: "), get_num("Второе число: ")
                res = MathOperations.sum_two(a, b)
            elif choice == "2":
                a, b = get_num("Уменьшаемое: "), get_num("Вычитаемое: ")
                res = MathOperations.subtract(a, b)
            elif choice == "3":
                a, b = get_num("Первый множитель: "), get_num("Второй множитель: ")
                res = MathOperations.multiply(a, b)
            elif choice == "4":
                a, b = get_num("Делимое: "), get_num("Делитель: ")
                res = MathOperations.divide(a, b)
            elif choice == "5":
                a, b = get_num("Основание: "), get_num("Степень: ")
                res = MathOperations.power(a, b)
            elif choice == "6":
                n = get_num("Число: ")
                res = MathOperations.fact(int(n))
            elif choice == "7":
                x = get_num("Угол в радианах: ")
                res = MathOperations.sin(x)
            elif choice == "8":
                nums = get_nums("Числа через пробел: ")
                res = MathOperations.med(nums)
            else:
                print("Неизвестная команда!")
                continue

            print(f"Результат: {res}")
            print("-" * 20)

        except Exception as e:
            print(f"Ошибка: {e}")
            print("-" * 20)


if __name__ == "__main__":
    run_calculator()