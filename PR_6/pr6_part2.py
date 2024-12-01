def heapify(arr, n, i):
    """
    Преобразует поддерево с корнем в индексе i в двоичную кучу.

    :param arr: Массив для преобразования.
    :param n: Размер кучи.
    :param i: Индекс корня поддерева.
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Сортирует массив методом пирамидальной сортировки.

    :param arr: Массив для сортировки.
    """
    n = len(arr)

    print("Построение максимальной кучи:")
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(arr)

    print("\nИзвлечение элементов:")
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print(f"Меняем местами {arr[i]} и {arr[0]}: {arr}")
        heapify(arr, i, 0)
        print(arr)

full_name = input("Введите ФИО студента: ")
letters = [char for char in full_name[:12] if char != ' ']
print("Исходный массив без пробелов:", letters)

heap_sort(letters)
print("\nОтсортированный массив без пробелов:", letters)