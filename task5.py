import cmath

def solve_quadratic_equation(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c

    # Расчет корней в зависимости от значения дискриминанта
    if discriminant >= 0:
        # Корни действительные
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    else:
        # Корни комплексные
        real_part = -b / (2*a)
        imaginary_part = cmath.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)

    return root1, root2

def main():
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))

    root1, root2 = solve_quadratic_equation(a, b, c)

    print("Корни уравнения:")
    print(f"Корень 1: {root1}")
    print(f"Корень 2: {root2}")

if __name__ == "__main__":
    main()
