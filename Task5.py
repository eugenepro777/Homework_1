'''Напишите программу, которая принимает на вход координаты
двух точек и находит расстояние между ними в 2D пространстве.

Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''
import math
from decimal import Decimal, ROUND_FLOOR

x1 = float(input('Введите значение х, точки А:\t'))
y1 = float(input('Введите значение y, точки А:\t'))
x2 = float(input('Введите значение х, точки B:\t'))
y2 = float(input('Введите значение y, точки B:\t'))

distance = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
dec_distance = Decimal(distance)
accurate_distance = dec_distance.quantize(Decimal("1.00"), ROUND_FLOOR)

print(f"Расстояние = {accurate_distance}")
