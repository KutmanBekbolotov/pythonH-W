a = float(input("Введите длину первой стороны треугольника: "))
b = float(input("Введите длину второй стороны треугольника: "))
c = float(input("Введите длину третьей стороны треугольника: "))

if a + b > c and b + c > a and c + a > b:
    print("Треугольник с такими сторонами существует.")
else:
    print("Треугольник с такими сторонами не существует.")