print('Cálculo para aumento de salário')
s = float(input('Qual o salário atual? '))
a = float(input('De quantos % será o aumento? '))
ns = s + (s * a / 100)
print('O novo salário será R$ {:.2f}'.format(ns))
