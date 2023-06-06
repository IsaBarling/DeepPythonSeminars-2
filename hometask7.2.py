def add_fractions(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split('/'))  # Разделение числителя и знаменателя первой дроби
    numerator2, denominator2 = map(int, fraction2.split('/'))  # Разделение числителя и знаменателя второй дроби
    
    common_denominator = denominator1 * denominator2  # Вычисление общего знаменателя
    sum_numerator = numerator1 * denominator2 + numerator2 * denominator1  # Вычисление числителя суммы
    
    return f"{sum_numerator}/{common_denominator}"  # Возвращение результата в формате "a/b"

def multiply_fractions(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split('/'))  # Разделение числителя и знаменателя первой дроби
    numerator2, denominator2 = map(int, fraction2.split('/'))  # Разделение числителя и знаменателя второй дроби
    
    product_numerator = numerator1 * numerator2  # Вычисление числителя произведения
    product_denominator = denominator1 * denominator2  # Вычисление знаменателя произведения
    
    return f"{product_numerator}/{product_denominator}"  # Возвращение результата в формате "a/b"

# Ввод дробей
fraction1 = input("Введите первую дробь (в формате a/b): ")
fraction2 = input("Введите вторую дробь (в формате a/b): ")

# Вычисление суммы и произведения дробей
sum_fraction = add_fractions(fraction1, fraction2)  
product_fraction = multiply_fractions(fraction1, fraction2)  

# Вывод результатов
print(f"Сумма дробей: {sum_fraction}")  
print(f"Произведение дробей: {product_fraction}")  

