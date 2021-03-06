def get_unique_elements(*, l1: list[int], l2: list[int]) -> list[int]:
    """
    Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом.
    Оценить эффективность своего решения.

    Пусть n - размер l1, m - размер l2

    Использую set, тк внутри это hashmap и позволяет быстро проверять есть ли в ней элемент.
    Создание сета - O(m) по времени
    Хранение сета - O(m) по памяти
    Пройтись по l1 - O(n) по времени

    Общая стоимость O(m + n) по времени
    """

    l2_set = set(l2)
    return [el for el in l1 if el not in l2_set]


def remove_zeros(l: list[int]):
    """
    Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти

    Алгоритм работает за линейное время O(n)

    list - это динамический массив. Удалить элемент из середины или начала массива - эта операция выполняется за O(n),
    тк нужно подвинуть все элементы стоящие справа от удаляемого. Но удаление элемента из конца массива выполняется за
    O(1) тк. правее уже ничего нет.

    За O(n) сдвигаем все нули вправа и запоминаем индекс первого нуля. Потом за линейное время удаляем все нули с конца
    """
    value_to_remove = 0
    l_length = len(l)

    i = 0
    pivot_i = 0

    while i < l_length:
        if l[i] != value_to_remove:
            l[i], l[pivot_i] = l[pivot_i], l[i]
            pivot_i += 1
        i += 1

    for i in range(l_length - 1, pivot_i - 1, -1):
        del l[i]
