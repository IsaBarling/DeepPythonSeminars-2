import math

def calculate_circle_properties(diameter: float):
    if diameter > 1000:
        diameter = 1000
    
    radius = diameter / 2
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    return area, circumference

def main():
    diameter = float(input("Введите диаметр круга: "))

    if diameter > 1000:
        print("Введите значение меньше 1000")
        return

    area, circumference = calculate_circle_properties(diameter)

    print(f"Площадь круга: {area:.42f}")
    print(f"Длина окружности: {circumference:.42f}")

if __name__ == "__main__":
    main()
