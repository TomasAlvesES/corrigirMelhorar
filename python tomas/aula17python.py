pessoa = {} #criando um dicionario vazio chamado pessoa

#todos esses dados serão armazenados no dicionario 
pessoa["nome"] = input("digitar o nome: ") #nome é chave e o que o usuario digitar sera valor associado 
pessoa["idade"] = int(input("digite sua idade: ")) #idade e chave e o que o usuario digitar sera valor assciado, usamos int pois sera um numero: ?
pessoa["cidade"] = input("digite sua cidade: ") #cidade e chave e o que o ususario digitar sera valor associado

print("\n --- dados cadastrados --- ")
#percorrendo o dicionario usado item(), chave = nome - valor = o conteudo guardado
for chave, valor in pessoa.items():
    print(f"{chave}:{valor}") #exibindo chave e valor formatados