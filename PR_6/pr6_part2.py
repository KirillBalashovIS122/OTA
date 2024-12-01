def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    l = 2 * i + 1  # Левый потомок
    r = 2 * i + 2  # Правый потомок

    # Если левый потомок больше корня
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Если правый потомок больше, чем самый большой элемент на данный момент
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Если самый большой элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами

        # Рекурсивно преобразуем в двоичную кучу затронутое поддерево
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение максимальной кучи
    print("Построение максимальной кучи:")
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(arr)

    # Один за другим извлекаем элементы
    print("\nИзвлечение элементов:")
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Меняем местами
        print(f"Меняем местами {arr[i]} и {arr[0]}: {arr}")
        heapify(arr, i, 0)
        print(arr)

# Ввод ФИО с клавиатуры
full_name = input("Введите ФИО студента: ")
letters = [char for char in full_name[:12] if char != ' ']  # Берем первые 12 символов и удаляем пробелы
print("Исходный массив без пробелов:", letters)

# Сортировка массива
heap_sort(letters)
print("\nОтсортированный массив без пробелов:", letters)