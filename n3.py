from typing import Any, List, Tuple, Dict, Union


def function_name(
        search: str,
        status: bool,
        *args: Any,
        **kwargs: Any
) -> Union[List[int], str]:
    """
    Обрабатывает аргументы в зависимости от параметров search и status.

    Параметры:
        search (str): Определяет режим обработки:
            - "args" - обработка позиционных аргументов
            - "kwargs" - обработка именованных аргументов
        status (bool): Флаг, определяющий тип обработки для режима "args":
            - True: фильтрация целых чисел
            - False: конкатенация всех аргументов
        *args: Произвольные позиционные аргументы
        **kwargs: Произвольные именованные аргументы

    Возвращает:
        Union[List[int], str]:
            - Для search="args" и status=True: список целых чисел
            - Для search="args" и status=False: строку из всех аргументов
            - Для search="kwargs": строку с описанием пар ключ-значение

    Исключения:
        ValueError: Если параметр search имеет недопустимое значение
    """
    result: List[int] = []
    result_2: str = ""

    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")