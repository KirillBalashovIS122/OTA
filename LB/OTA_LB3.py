import time
import random
import math

# Метод сортировки расческой
def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.247330950103979
    sorted = False
    comparisons = 0
    swaps = 0

    while not sorted:
        gap = math.floor(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            comparisons += 1
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swaps += 1
                sorted = False
            i += 1

    return comparisons, swaps

# Метод гномьей сортировки
def gnome_sort(arr):
    n = len(arr)
    i = 0
    comparisons = 0
    swaps = 0

    while i < n:
        comparisons += 1
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            swaps += 1
            i -= 1

    return comparisons, swaps

# Метод "глупой" сортировки
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogo_sort(arr):
    comparisons = 0
    swaps = 0

    while not is_sorted(arr):
        random.shuffle(arr)
        swaps += 1
        comparisons += len(arr) - 1

    return comparisons, swaps

# Ввод исходных данных
def input_data():
    choice = input("Выберите способ ввода данных (1 - из файла, 2 - с консоли, 3 - случайные числа): ")
    if choice == '1':
        filename = input("Введите имя файла: ")
        with open(filename, 'r') as file:
            data = list(map(int, file.read().split()))
    elif choice == '2':
        data = list(map(int, input("Введите числа через пробел: ").split()))
    elif choice == '3':
        size = int(input("Введите размер массива: "))
        data = [random.randint(0, 100) for _ in range(size)]
    else:
        print("Неверный выбор.")
        return None
    return data

# Основная программа
def main():
    data = input_data()
    if data is None:
        return

    print("Исходный массив:", data)

    choice = input("Выберите метод сортировки (1 - расческа, 2 - гномья, 3 - глупая): ")
    start_time = time.time()

    if choice == '1':
        comparisons, swaps = comb_sort(data)
    elif choice == '2':
        comparisons, swaps = gnome_sort(data)
    elif choice == '3':
        comparisons, swaps = bogo_sort(data)
    else:
        print("Неверный выбор.")
        return

    end_time = time.time()
    print("Отсортированный массив:", data)
    print("Время выполнения:", end_time - start_time, "секунд")
    print("Количество сравнений:", comparisons)
    print("Количество перестановок:", swaps)

if __name__ == "__main__":
    main()