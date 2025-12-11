#simulador de emprestimo Bancario

#solicitação de entradas que serão armazenadas nas variantes
print(" === sistema de analise de credito === ")
nome = input("nome do cliente: ")
renda = float(input("informe sua renda mensal do cliente: R$"))
valor_pedido = float(input("informe o valor do emprestimo desejado: R$"))
parcelas = int(input("informe o numero de parcelas: "))
historico = input("possui nome sujo? (sim/não): ")

#calculo do valor da parcela
valor_parcela = valor_pedido/parcelas

#print(f"\n cliente: {nome}")
#print("\n cliente: {nome}",nome, "lorem ipsum")

#exibe um resumo inicial do cliente
print(f"\n cliente: {nome}")
print(f"valor do emprestimo: R$ {valor_pedido:.2f}")
print(f"parcelas: {parcelas}x de R$ {valor_parcela:.2f}")

#verifica primeiro se o nome esta limpo
if historico == "sim":
    print("emprestimo negado! nome com restrição.")
else:
    #verifica se a parcela não ultrapassa 40% da renda
    if valor_pedido > renda*0.3:
        print("emprestimo negado! parcelas comprometem mais de 30% da renda.")
    else:
        #verifica valor do emprestimo em relação a renda
        if valor_pedido > renda*20:
            print("emprestimo negado! valor muito alto para a renda informada. ")
        elif renda >= 5000 and valor_pedido <= 10000:
            print("emprestimo aprovado com taxa reduzida! cliente perfil premium")
        elif renda >= 3000 and renda < 5000:
            print("emprestimo aprovado com taxa padrão. ")
        else:
            print("emprestimo aprovado com taxa elevado (cliente de risco). ")

print (" \n --- analise concluida --- ")    