def sieve_of_eratosthenes(n):
    """Реализация решета Эратосфена для нахождения всех простых чисел до n."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes


def euclidean_algorithm(a, b):
    """Реализация алгоритма Евклида для нахождения НОД двух чисел."""
    while b != 0:
        a, b = b, a % b
    return a


def fast_exponentiation(x, n):
    """Реализация алгоритма быстрого возведения в степень."""
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result


def main_menu():
    """Главное меню программы."""
    while True:
        print("\nНачальное меню:")
        print("1. Алгоритм решета Эратосфена")
        print("2. Алгоритм Евклида")
        print("3. Алгоритм быстрого возведения в степень")
        print("4. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            n = int(input("Введите число n для нахождения простых чисел до n: "))
            primes = sieve_of_eratosthenes(n)
            print(f"Простые числа до {n}: {primes}")
        elif choice == "2":
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            gcd = euclidean_algorithm(a, b)
            print(f"НОД({a}, {b}) = {gcd}")
        elif choice == "3":
            x = int(input("Введите число x: "))
            n = int(input("Введите степень n: "))
            result = fast_exponentiation(x, n)
            print(f"{x} в степени {n} = {result}")
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню от 1 до 4.")


if __name__ == "__main__":
    main_menu()
