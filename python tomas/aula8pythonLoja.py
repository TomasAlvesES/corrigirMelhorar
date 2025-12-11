print ("\n --- lojas uga senai --- ")
valor = float(input("digite o valor total da compra (R$): "))
forma_pagamento = input("forma do pagamento (dinheiro/cartão/pix) ")

if forma_pagamento == "dinheiro":
    total = valor*0.90
    print("pagamento a vista em dinheiro. desconto da 10% aplicado! ")
elif forma_pagamento == "pix":
    if valor >= 1000:
        total = valor*0.85
        print("pagamento via pix: desconto de 15% aplicado! ")
    elif valor >= 500 and valor < 1000:
        total = valor*0.90
        print("pagamento via pix: desconto de 15% aplicado! ")
    else:
        total = valor*0.95
        print("pagamento via pix: desconto de 5% aplicado! ")
elif forma_pagamento == "debito":
    total = valor
    print("pagamento a vista no cartão de debito!")
elif forma_pagamento == "credito":
    parcelas = int(input("em quantas vezes deseja parcelar? "))
    if parcelas <= 3:
        total = valor
        print("parcela em ate 3x sem juros! ")
    elif 4<= parcelas <=6:
        total = valor*1.1
        print("parcelamento de 4 a 6x com 10% de juros")
    else:
        total = valor*1.20
        print("parcelamento de 4 a 6x com 20% de juros")
else:
    print ("forma de pagamento invalida! tente novamente usando outra opção. ")

print (f"valor finaol a pagar: R$ {total:.2f}")
