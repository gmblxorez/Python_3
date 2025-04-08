from typing import List, Union, TypeVar

T = TypeVar('T', int, float, str)


def multiply_elements(
        items: List[T],
        factor: Union[int, float] = 2
) -> List[T]:

    return [item * factor for item in items]


def main() -> None:
    """Основная логика ввода/вывода."""
    # Ввод списка
    input_data = input("Введите числа через пробел: ").strip()
    if not input_data:
        print("Вы ничего не написали")
        return

    try:
        elements = [int(x) if x.isdigit() else float(x) for x in input_data.split()]
    except ValueError:
        print("Нужно написать числа!")
        return

    # Ввод множителя
    factor_input = input("Введите множитель (по умолчанию 2): ").strip()
    factor = 2 if not factor_input else float(factor_input)

    # Вызов основной функции
    result_func = multiply_elements(elements, factor)
    print(f"Результат (функция): {result_func}")

    # Лямбда-версия
    multiply_lambda = lambda lst, m: list(map(lambda x: x * m, lst))
    result_lambda = multiply_lambda(elements, factor)
    print(f"Результат (лямбда-функция): {result_lambda}")


if __name__ == "__main__":
    main()