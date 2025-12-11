numeros = ()

print ("--- digite 5 numeros ---")
for i in range(5):
    n = int(input(f"digite o {i+1}° numeros: "))
    numeros += (n, )

print(f"numeors digitados: {numeros}")
print(f"maior numeros é {max(numeros)}")
print(f"menor numeros é {min(numeros)}")

contador = 0

if numeros == 5:
    contador += 1

print(f"o numro 5 apareceu {contador} vezes. ")