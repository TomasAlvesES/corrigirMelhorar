#objetivo: criar um programa de gerenciamentio de notas e mostrar o uso de len(), append(), sum(), remove()

#lista vazia para armazenar as notas

print(" --- gerenciador de notas --- ")

while True:
    print("\n menu de opções: ")
    print("1 - adicionar nota ")
    print("2 - remover nota ")
    print("3 - mostrar todas as notas ")
    print("4 - mostrar a quantidade das notas ")
    print("5 - sair ")

    opcao = int(input("escolha uma opção: "))

    #se a opção for igual a 1, adicionar nota
    if opcao == 1:
        notas = float(input("digite a nota: "))
        notas.append(notas)
        print("nota adicionada com sucesso")

    #remover nota
    elif opcao == 2:
        if len(notas) == 0:
            print("não ha notas para remover!")
        else:
            print("notas atuais: ",notas)
            remover = float(input("digite a nota que deseja remover: "))
            if remover in notas:
                notas.remove(remover)
                print(f"nota{remover} removida com sucesso!")
            else:
                print("essa nota não esta na lista.")

#mostrar notas
    elif opcao == 3:
        if len(notas) == 0:
            print("nenhuma nota cadastrada ainda.")
        else:
            print("notas cadastradas: ",notas)

    #mostrar quantidade e media
    elif opcao == 4:
        if len(notas) == 0:
            print("nenhuma nota cadastrada ainda para calcular a media.")
        else:
            quantidade = len(notas)
            soma = sum(notas)
            media = soma/quantidade
            print(f"quantidade de notas: {quantidade}")
            print(f"soma das notas: {soma:.2f}")
            print(f"media da turma: {media:.2f}")

            if media >= 7:
                print("a turma esta com um bom desempenho")
            else:
                print("a turma precisa melhorar")

#sair
    elif opcao == 5:
        print("encerrando o programa. ate mais!")
        break
    else:
        print("opção invalida, tente novamente")

