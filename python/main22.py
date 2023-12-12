
try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Por favor digitar apenas números.')

else:
    print('Usurario digitou um valor correto.')
    resultado = valor * 2
    print(resultado)