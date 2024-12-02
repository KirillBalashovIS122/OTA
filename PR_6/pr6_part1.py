import timeit
import random

def insertion_sort(arr):
    """
    Сортирует массив методом прямого включения (Insertion Sort).

    :param arr: Список элементов для сортировки.
    :return: Отсортированный список.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def shell_sort(arr):
    """
    Сортирует массив методом Шелла (Shell Sort).

    :param arr: Список элементов для сортировки.
    :return: Отсортированный список.
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

fio = input("Введите ФИО студента: ")
fio = fio.replace(" ", "")[:12]
arr = list(fio)
print("Исходный массив без пробелов:", ''.join(arr))

insertion_sorted_arr = arr.copy()
insertion_sort(insertion_sorted_arr)
print("Отсортированный массив (прямое включение):", ''.join(insertion_sorted_arr))

shell_sorted_arr = arr.copy()
shell_sort(shell_sorted_arr)
print("Отсортированный массив (Шелла):", ''.join(shell_sorted_arr))

insertion_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1000)
print(f"Время выполнения Insertion Sort: {insertion_time:.6f} секунд")

shell_time = timeit.timeit(lambda: shell_sort(arr.copy()), number=1000)
print(f"Время выполнения Shell Sort: {shell_time:.6f} секунд")

print("\nСравнение времени работы методов:")
print(f"Insertion Sort: {insertion_time:.6f} секунд")
print(f"Shell Sort: {shell_time:.6f} секунд")

sizes = [100, 500, 1000, 5000, 10000]

results = {
    "Insertion Sort": [],
    "Shell Sort": []
}

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]
    
    insertion_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=10)
    results["Insertion Sort"].append(insertion_time)
    
    shell_time = timeit.timeit(lambda: shell_sort(arr.copy()), number=10)
    results["Shell Sort"].append(shell_time)

print("\nСравнение времени работы методов для разных размеров массивов:")
print("Размер массива | Insertion Sort | Shell Sort")
for i, size in enumerate(sizes):
    print(f"{size} | {results['Insertion Sort'][i]:.6f} | {results['Shell Sort'][i]:.6f}")