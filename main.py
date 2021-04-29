from math import sqrt

best_ppi_no_retita = 110
best_ppi_with_retina = 220

width = float(input('Width: '))
height = float(input('Height: '))
diagonal = float(input('Diagonal in inches: '))

result = sqrt(width ** 2 + height ** 2) / diagonal

print('Your ppi: ', round(result))
print('Best ppi no retina: ', best_ppi_no_retita)
print('Best ppi with retina: ', best_ppi_with_retina)

