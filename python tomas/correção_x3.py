meses = ("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","novembro","outubro","dezembro")

print(" --- meses do ano --- ")

while True:
    numero = int(input("digite um numero entre 1 e 12 para saber o mes correspondente: (informe -1 para sair)"))

    if numero == -1:
        print("encerrado o sistema! ")
        break

    if numero >= 1 and numero <= 12:
        print(f"o mes correspondente é: {meses[numero - 1]}") #serve para pegar o numero informado pelo usuario e subtrair -1 para pegar o valor certo, pois nossa tupla começa com 0
    else:
        print("numero invalido! digite novamente entre 1 a 12: ...")