produtos = [{"nome":"cafe", "preco": 25.96, "categoria":"alimentos", "estoque":30}
            {"nome": "detergente", "preco" : 2.99, "categoria" :"limpeza", "estoque" : 50}
            {"nome": "sabão em pó", "preco" : 17.99, "categoria" :"limpeza", "estoque" : 8}
            {"nome": "pão", "preco" : 7.99, "categoria" :"alimentos", "estoque" :15}]


print(" --- lista de produtos --- ")
for i in produtos:
    print("---------------------------------")
    for chave, valor in i.items(): #serve para pegar chave e valor dentro
        print(f"{chave}:{valor}")

