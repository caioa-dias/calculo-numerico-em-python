# Importação das bibliotecas
from math import fabs, pow

# Definição dos valores limitantes do intervalo de chute inicial:
a = 0.6     # Início do intervalo
b = 0.75    # Final do intervalo

# Definição do valor de erro desejado:
erro = fabs((b-a)/(b+a)*100)

# Definição do contador de iteraçãoes:
i = 0

# Definição da função estudada:
def function(h):
    return (pow(0.0002, 1/2)/0.03)*((pow(20*h, 5/3))/(pow(20 + 2 * h, 2/3))) - 5

# Método da Bissecção:
while erro > 0.00001:
    p = ((a+b)/2)
    if function(a) * function(p) < 0:
        b = p
    elif function(a) * function(p) > 0:
        a = p
    elif function(a) * function(p) == 0:
        break
    i += 1
print("O valor da raíz é:", p, "\nEsse resultado foi encontrado após", i, "iterações.")
