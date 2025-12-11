numeros = () #criação de tupla com o nome numeros que ira guardar numeros fornecidos pelo usuario

#estrutura do repetição para permitir que o usurio digite vaios numeros
while True:
    n = int(input("digite um numero (ou -1 para sair): "))
    #se o usuario digitar -1, o laço é interrompido (break)
    if n == -1:
        break
    numeros += (n,) #como tuplas são imutaveis não usamos append(), em vez disso criamos uma nova tupla com o numero adicionado
    
#apos sair do loop, verificamos se a tupla esta vazia ou não    
if len(numeros) > 0:
    print("\n=== resultados ===")
    print(f"numeros digitados: {numeros}")
    print(f"quantidade: {len(numeros)}")
    print(f"soma: {sum(numeros)}")
    print(f"maior numero: {max(numeros)}")
    print(f"menor numero: {min(numeros)}")

    media = sum(numeros)/len(numeros)

    if media >= 50:
        print(f"media: {media:.2f} -> alta!")
    else:
        print(f"media: {media:.2f} -> baixa!")

else:
    print("nenhum numero foi adicionado!")
