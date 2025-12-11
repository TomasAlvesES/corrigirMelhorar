#solivita ao usuario que informe a hora atual (apenas o numero da hora)
hora = int(input("digite a hora atual (0 a 23): "))

#estrutura condicional para verificar o periodo do dia
if hora <=12:
    print("bom dia! ")
elif hora > 12 and hora < 18:
    print("boa tarde!")
else:
    print("boa noite! ")