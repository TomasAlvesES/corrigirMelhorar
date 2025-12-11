nomes = []
salarios = []

while True:
    nome = input("digite o nome funcionario: (ou 'sair' para encerrar)")

    if nome == "sair":
        print("programador finalizado!")
        break

    nomes.append(nomes)

    salarios = float(input("digite o salariio do funcionario"))

    salarios.append(salarios)

print(f"o total de funcionarios cadastrados é: {len(nomes)} ")
print(f"a media salarial dos funcionarios é: {sum(salarios)/len(salarios)}")
print(f"o maior salario é: {max(salarios)}")
print(f"o menor salario é: {min(salarios)}")