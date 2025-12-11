nomes = []

while True:
    n = input("digite o nome que deseja (digite sair para encerrar): ")
    nomes.append(n)
    if n == "sair":
        print("encerrando o programa ")
        break 
    nomes.append(n)

print(f"a quantidade de nomes informados {len(nomes)}.")
print(f"a lista completa de nomes é: {nomes}")

