'''
Напишите программу для. проверки истинности
утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''

for i in 0, 1:
    for j in 0, 1:
        for k in 0, 1:
            expression_1 = not (k or j or i)
            expression_2 = (not k) and (not j) and (not i)
            if expression_1 == expression_2:
                print('NOT (', i, 'OR', j, 'OR', k, ')', '=', 'NOT', i, 'AND NOT', j, 'AND NOT', k)
                print('утверждение верно,', int(expression_1), '=', int(expression_2), '\n')
            else:
                print('утверждение неверно', int(expression_1), '!=', int(expression_2), '\n')

