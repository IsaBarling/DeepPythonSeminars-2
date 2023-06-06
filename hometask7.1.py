def decimal_to_hex(decimal):
    hex_digits = "0123456789ABCDEF"
    hex_string = ""

    if decimal == 0:
        hex_string = "0"
    else:
        while decimal > 0:
            remainder = decimal % 16
            hex_digit = hex_digits[remainder]
            hex_string = hex_digit + hex_string
            decimal = decimal // 16

    return hex_string

# Тестирование программы
number = int(input("Введите целое число: "))

hexadecimal = decimal_to_hex(number)

print(f"Шестнадцатеричное представление числа: {hexadecimal}")
