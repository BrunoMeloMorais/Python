# Python
 valor = int(input('Digite o valor do seu produto que deseja colocar a venda'))

while valor > 25:
  valor = (valor * 0.10) + valor
  print(f' O valor final do seu porduto é de ${valor}')
  break
