def convert_to_binary(num: int) -> str:
    return bin(num)[2:]  # Используем срез, чтобы удалить префикс '0b'


def convert_to_octal(num: int) -> str:
    return oct(num)[2:]  # Используем срез, чтобы удалить префикс '0o'


def main():
    num = int(input("Введите целое число: "))
    binary = convert_to_binary(num)
    octal = convert_to_octal(num)

    print(f"Двоичное представление числа: {binary}")
    print(f"Восьмеричное представление числа: {octal}")


if __name__ == "__main__":
    main()
