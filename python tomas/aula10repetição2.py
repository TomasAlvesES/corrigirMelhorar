#inicia um loop que vai se repetir enquanto a condição for verdadeira 
while True: #true e uma condiçõ booleana que sempre e verdadeira, logo esse loop sera ifinito
    print(" --- login --- ")
    nome = input("usuario: ")
    senha = input("senha: ")

#condição que faz uma comparação para verificar se ambas condições são verdadeiras
    if nome == "admin" and senha == "1234":
        print("login realizado com sucesso! ")
        break #comando que interrompe o loop0
    else: 
        print("ususario ou senha incorreta! tente novamente")