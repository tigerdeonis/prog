def check_number(n):
    """Определяет, является ли число четным или нечетным"""
    if n % 2 == 0:
        return f"Число {n} — четное."
    else:
        return f"Число {n} — нечетное."

def main():
    try:
        number = int(input("Введите число: "))
        print(check_number(number))
    except ValueError:
        print("Ошибка: ")

if __name__ == "__main__":
    main()
