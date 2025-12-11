#criação de programa que permita que p usuario consulte o preço de um produto digitando o nome.


#duas tuplas paralelas: uma com os nomes dos produtos e a outra com os preços

produtos = ("arroz","feijão","macarrão","leite","pão","ovo")
precos = (5.50, 7.90, 4.20, 6,30, 3.00, 19.96)

#exibe a lista completa com seus preços 
print("\n --- lista de produtos --- ")
for i in range(len(produtos)):
    #percorre as posições (0 ate 15) e exibe o produto e o preço correspondente
    print(f"{produtos[i]} - {precos[i]:.2f}")

#inicia um loop para permitir varias consultas do usuarios
while True:
    nome = input("\nDigite o nome para ver o preço (ou 'sair'): ").lower()
    #metodo .lower() transforma o texto em minusculas para evitar erro de comparação

    #se o usuario digitar 'sair', o programa 
    if nome == "sair":
        print(f"programa encerrado. ")
        break

    #verifica se o produto existe dentro da tupla 'produtos'
    if nome in produtos:
        indice = produtos. index(nome) #se o produto existe, encontramos sua posisão em index()
        print(f"o preço de {nome} e R$ {precos[indice]:.2f}.")
    else:
        print("produto não encontrado.")