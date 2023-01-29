'''
 Напишите программу, которая по заданному 
номеру четверти, показывает диапазон возможных
координат точек в этой четверти (x и y). 
'''

quarter_number = input('Введите номер четверти: ')

if quarter_number == '1' or quarter_number == 'I':
    print('x > 0 и y > 0')
elif quarter_number == '2' or quarter_number == 'II':
    print('x < 0 и y > 0')
elif quarter_number == '3' or quarter_number == 'III':
    print('x < 0 и y < 0')
elif quarter_number == '4' or quarter_number == 'IV':
    print('x > 0 и y < 0')
else:
    print('введите арабскую или римскую цифру')