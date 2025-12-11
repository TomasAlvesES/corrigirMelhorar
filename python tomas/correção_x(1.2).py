#nomes = ("Ana","Breno","Carlos","Daniela","Enzo") tupla com nomes difinidos

nomes = () #tupla vazia
 
print(" --- lista  de nomes --- ")
#print(nomes) mostra a tupla com os nomes

#estrutura de repetição que vai rodar 5 vezes pedindo nomes
for i in range(5):
    nomes = input(f"digite o {i+1}° nome: ")
    nomes += (nomes, ) #adiciona os nomes informados pelo usuario a tupla

print(f"nomes cadastrados: {nomes}")
print(f"primeiro nome - {nomes[0]}")
print(f"ultimo nome - {nomes[-1]}")
print(f"a quantidade total de nomes é: {len(nomes)}")