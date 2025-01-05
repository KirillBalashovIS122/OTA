# Функция двоичного поиска (Версия 1)
def binary_search_v1(arr, x):
    L, R = 0, len(arr) - 1
    found = False
    
    while L <= R:
        m = (L + R) // 2
        if arr[m] == x:
            found = True
            break
        elif arr[m] < x:
            L = m + 1
        else:
            R = m - 1
    
    return found

# Функция двоичного поиска (Версия 2)
def binary_search_v2(arr, x):
    L, R = 0, len(arr) - 1
    
    while L < R:
        m = (L + R) // 2
        if arr[m] < x:
            L = m + 1
        else:
            R = m
    
    if arr[R] == x:
        return True
    else:
        return False

# Основная программа
if __name__ == "__main__":
    # Ввод ФИО с клавиатуры
    fio = input("Введите ваше ФИО: ")

    # Удаляем пробелы и берём первые 12 символов, затем сортируем
    data = sorted(fio.replace(" ", "")[:12])
    print("Отсортированный массив (без пробелов):", data)

    # Поиск первой буквы имени и буквы «Я»
    first_name_letter = input("Введите первую букву вашего имени: ")
    letter_ya = 'Я'

    # Тестирование первой версии
    print("\nВерсия 1:")
    print(f"Буква '{first_name_letter}' найдена:", binary_search_v1(data, first_name_letter))
    print(f"Буква '{letter_ya}' найдена:", binary_search_v1(data, letter_ya))

    # Тестирование второй версии
    print("\nВерсия 2:")
    print(f"Буква '{first_name_letter}' найдена:", binary_search_v2(data, first_name_letter))
    print(f"Буква '{letter_ya}' найдена:", binary_search_v2(data, letter_ya))
