print("Esse programa tem a função de resolver uma equações do 2º grau.")
a = int(input("Informe o valor da variavel A: "))
b = int(input("Informe o valor da variavel B: "))
c = int(input("Informe o valor da variavel C: "))

delta = b**2 - 4*a*c

if delta < 0:
  print("Erro! O valor de delta não pode ser negativo!")
else:
  r1=(-b-(delta**0.5))/(2*a)
  r2=(-b+(delta**0.5))/(2*a)
  print("O valor das soluções são:",r1,"e",r2)