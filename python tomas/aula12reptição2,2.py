print("\n cadastro de usuario\n")
usuario_cadastro = input("crie seu nome de usuario: ").strip().lower()

while True:
    senha_cadastarda = input("crie uma senha de usuario (max. 8 caracteres): ").strip()
    if len(senha_cadastarda) <= 8:
        print("\n usuario cadastrado com sucesso!\n")
        break
    else:
        print("senha muito longa! digite uma senha com 8 caracteres.\n")

print("\n --- login --- \n")
#inicia um loop que vai se repetir enquanto a condição for verdadeira 
while True: #true e uma condiçõ booleana que sempre e verdadeira, logo esse loop sera ifinito
    print(" --- login --- ")
    nome = input("usuario: ").strip().lower()
    senha = input("senha: ").strip()

#condição que faz uma comparação para verificar se ambas condições são verdadeiras
    if nome == usuario_cadastro and senha == senha_cadastarda:
        print(f"login realizado com sucesso!\n bem vindo {nome}")
        break #comando que interrompe o loop
    else: 
        print("ususario ou senha incorreta! tente novamente")