import random
import time

def bubble_sort(arr):
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
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        # Проход слева направо
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        # Проход справа налево
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

def generate_array(size, order='random'):
    if order == 'ascending':
        return list(range(size))
    elif order == 'descending':
        return list(range(size, 0, -1))
    else:
        return [random.randint(0, size) for _ in range(size)]

def manual_sort():
    # Запрашиваем ФИО с клавиатуры
    full_name = input("Введите ваше ФИО: ")
    # Извлекаем первые 12 символов
    name_chars = list(full_name[:12])
    
    # Создаем копии для сортировки
    bubble_name_chars = name_chars.copy()
    shaker_name_chars = name_chars.copy()
    
    # Выполняем пузырьковую сортировку
    bubble_sort(bubble_name_chars)
    print("Результат пузырьковой сортировки:", ''.join(bubble_name_chars))
    
    # Выполняем шейкерную сортировку
    shaker_sort(shaker_name_chars)
    print("Результат шейкерной сортировки:", ''.join(shaker_name_chars))

def main():
    # Выполняем ручную сортировку
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