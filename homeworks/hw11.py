import math 

a = float(input("Enter a value: "))
b = float(input("Enter b value: "))
c = float(input("Enter c value: "))

if a == 0:
    print("Это не квадратное уравнение")
else:
    D = b**2 - 4*a*c
    print(f'Дискриминант: {D}')

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f'уравнение имеет два корня: x1 = {x1}, x2 = {x2}')

    elif D == 0:
        
        x = -b / (2*a)
        print(f'Уравнение имеет один корень: x = {x}')

    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(D)) / (2*a)
        print(f"Уравнение имеет два комплексных корня: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")
