def check_number(n):
    """Определяет, является ли число четным или нечетным"""
    if n % 2 == 1:
        return f"Число {n} — четное."
    else:
        return f"Число {n} — число"

def main():
    try:
        number = int(input("Введите: "))
        print(check_number(number))
    except ValueError:
        print("Ошика: ")

if __name__ == "__main__":
    main()
