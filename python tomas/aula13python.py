#exemplo de lista
'''numeros = [10,20,30,40,50] #criei uma lista com numeros inteiros (int)
print(numeros)
print(numeros[0]) #acessando a lista e pegando o primeiro valor dela
numeros[1] = 15
numeros[3] = 25

print(numeros)

#---------------------

#exemplos de tupla
coordenadas = (3,7)
print(coordenadas[0])
print(coordenadas[1])
coordenadas[0] = 13
coordenadas[0] = 17
print(coordenadas)
'''

#---------------------

#append() - metodo que serve para adicionar um novo elemento ao final da lista
#remove() - metodo que remove um elemento da lista
paises = ["brasil","argentina"]
print(paises)
paises.append("russia")
print(paises)
paises.remove("argentina")
print(paises)

if "italia" in paises:
    paises.remove("italia")
else:
    print("pais não existe")

'''if "brasil" in paises:
    paises.remove("italia")
else:
    print("pais não existe")
'''

numeros = [10,20,30]
print("quantidade de numeros: ", len(numeros))

#len() - metodo que seve para contagem de caracteres, numeros, letras, palavras...
#sum() - metado que serve para somar os elementos numericos

notas = [7.5,8.5,10]
print("soma das notas é: ",sum(notas))
print(f"a media de notas e: , {sum(notas)/len(notas):.2f}")



