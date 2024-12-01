import random
import time

def bubble_sort(arr):
    """
    Сортирует массив методом пузырьковой сортировки.

    :param arr: Массив для сортировки.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def shaker_sort(arr):
    """
    Сортирует массив методом шейкерной сортировки.

    :param arr: Массив для сортировки.
    """
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1

def measure_time(sort_func, arr):
    """
    Измеряет время выполнения сортировки.

    :param sort_func: Функция сортировки.
    :param arr: Массив для сортировки.
    :return: Время выполнения сортировки.
    """
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

def generate_array(size, order='random'):
    """
    Генерирует массив заданного размера и порядка.

    :param size: Размер массива.
    :param order: Порядок элементов ('ascending', 'descending', 'random').
    :return: Сгенерированный массив.
    """
    if order == 'ascending':
        return list(range(size))
    elif order == 'descending':
        return list(range(size, 0, -1))
    else:
        return [random.randint(0, size) for _ in range(size)]

def manual_sort():
    """
    Выполняет ручную сортировку введенного ФИО с использованием пузырьковой и шейкерной сортировок.
    """
    full_name = input("Введите ваше ФИО: ")
    name_chars = list(full_name[:12])
    
    bubble_name_chars = name_chars.copy()
    shaker_name_chars = name_chars.copy()
    
    bubble_sort(bubble_name_chars)
    print("Результат пузырьковой сортировки:", ''.join(bubble_name_chars))
    
    shaker_sort(shaker_name_chars)
    print("Результат шейкерной сортировки:", ''.join(shaker_name_chars))

def main():
    """
    Основная функция для выполнения ручной сортировки и сравнения времени выполнения пузырьковой и шейкерной сортировок.
    """
    manual_sort()
    
    sizes = [100, 1000, 10000]
    orders = ['ascending', 'descending', 'random']

    for size in sizes:
        print(f"Размер массива: {size}")
        for order in orders:
            arr = generate_array(size, order)
            arr_copy = arr.copy()

            bubble_time = measure_time(bubble_sort, arr)
            print(f"Пузырьковая сортировка ({order}): {bubble_time:.6f} сек")

            shaker_time = measure_time(shaker_sort, arr_copy)
            print(f"Шейкерная сортировка ({order}): {shaker_time:.6f} сек")

            print()

if __name__ == "__main__":
    main()