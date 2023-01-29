'''
Напишите программу, которая принимает на вход координаты
точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
плоскости, в которой находится эта точка (или на какой оси она находится)
Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''

coordinate_1 = float(input('Введите координату x = '))
coordinate_2 = float(input('Введите координату y = '))

if coordinate_1 > 0 and coordinate_2 > 0:
    print('I четверть')
elif coordinate_1 < 0 and coordinate_2 > 0:
    print('II четверть')
elif coordinate_1 < 0 and coordinate_2 < 0:
    print('III четверть')
elif coordinate_1 > 0 and coordinate_2 < 0:
    print('IV четверть')
elif coordinate_1 == 0 and coordinate_2 != 0:
    print('точка находится на оси y')
elif coordinate_2 == 0 and coordinate_1 != 0:
    print('точка находится на оси x')
elif coordinate_1 == coordinate_2 == 0:
    print('точка в центре координат')

     