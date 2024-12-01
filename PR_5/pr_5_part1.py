def selection_sort(arr):
    """
    Сортирует массив методом прямого выбора, игнорируя пробелы.

    :param arr: Массив символов для сортировки.
    :return: Отсортированный массив с пробелами на своих местах.
    """
    arr_no_spaces = [char for char in arr if char != ' ']
    n = len(arr_no_spaces)
    
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr_no_spaces[j] < arr_no_spaces[min_index]:
                min_index = j
        arr_no_spaces[i], arr_no_spaces[min_index] = arr_no_spaces[min_index], arr_no_spaces[i]
    
    arr_sorted = []
    space_indices = [i for i, char in enumerate(arr) if char == ' ']
    space_index = 0
    for char in arr_no_spaces:
        while space_index < len(space_indices) and space_indices[space_index] == len(arr_sorted):
            arr_sorted.append(' ')
            space_index += 1
        arr_sorted.append(char)
    
    while space_index < len(space_indices):
        arr_sorted.append(' ')
        space_index += 1
    
    return arr_sorted

def checksum(arr):
    """
    Подсчитывает контрольную сумму массива, игнорируя пробелы.

    :param arr: Массив символов.
    :return: Контрольная сумма.
    """
    return sum(ord(char) for char in arr if char != ' ')

while True:
    full_name = input("Введите ФИО студента: ")
    if len(full_name) >= 12:
        break
    else:
        print("ФИО должно содержать не менее 12 символов. Попробуйте снова.")

arr = list(full_name[:12])
print("Исходный массив (без пробелов):", [char for char in arr if char != ' '])

arr_sorted = selection_sort(arr)
print("Отсортированный массив (без пробелов):", [char for char in arr_sorted if char != ' '])

initial_checksum = checksum(list(full_name[:12]))
sorted_checksum = checksum(arr_sorted)

print("Контрольная сумма исходного массива:", initial_checksum)
print("Контрольная сумма отсортированного массива:", sorted_checksum)

if initial_checksum == sorted_checksum:
    print("Сортировка выполнена правильно.")
else:
    print("Ошибка в сортировке.")