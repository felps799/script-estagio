# Calcular subtotal, desconto e total, recusando valores negativos com uma mensagem compreensível.
subtotal = float(input('Digite o subtotal: '))
if subtotal <= 0:
    print('O subtotal não pode ser zero ou negativo. Por favor, insira um valor válido.')
else:
    desconto = float(input('Digite o desconto em porcentagem: '))
    if desconto <= 0:
        print('O desconto não pode ser zero ou negativo. Por favor, insira um valor válido.')
    else:
        print(f"O total do pedido é de R${subtotal - (subtotal * desconto / 100):.2f}")
