import os
os.system("cls || clear")

comanda = 0
contador = 0
comida = " " 
codigos_pratos = " "


while True:
    cardapio = int(input("""
Selecione o prato que deseja:
Código \t Prato \t\t Preço
1 \t Lasanha \t R$25                    
2 \t Feijoada \t R$25                     
3 \t Frango Assado \t R$18                     
4 \t Pizza \t\t R$23                     
5 \t Parmegiana \t R$30                   
6 \t Sushi \t\t R$120                    
7 \t Miojo \t \t R$3  

"""))   
    
    match cardapio:
        case 1 :
            comanda += 25
            contador += 1
            prato = "Lasanha (1º)"
            codigos = "1"
        case 2:
            prato = "Feijoada (2º)"
            comanda += 25
            contador += 1
            codigos = "2"
        case 3:
            prato = "Frango  assado (3º)"
            contador += 1
            comanda += 18
            codigos ="3"
        case 4:
            prato = "Pizza (4º)"
            contador += 1
            comanda += 23
            codigos ="4"
        case 5:
            prato = "Parmegiana (5º)"
            contador += 1
            comanda += 30
            codigos ="5"
        case 6:
            prato = "Sushi (6º)"
            contador += 1
            comanda += 120
            codigos ="6"
        case 7:
            prato = "Miojo (7º)"
            contador += 1
            comanda += 3
            codigos ="7"
        case _:
            print("codigo invalido.")
            
        
    
    comida += prato + " " 
    codigos_pratos += codigos + " "
    permissao = int(input("Deseja pedir mais um prato? Digite '0' para encerrar a comanda, caso queira prosseguir, digite '1': "))

    if permissao == 0:
     break

    
pagamento = int(input("Qual a forma de pagamento  ? 1 para avista e 2 para cartão de credito: "))
    
match pagamento:
    case 1:
        pagamento = "Á vista"
        desconto = comanda * 0.1
        desconto2 = comanda - (comanda * 0.1)
        print(f"\nSeu desconto foi de: {desconto}")
        print(f"Sua comando deu no total: {desconto2} ")
        print(f" Valot total comanda {comanda}")
        print(f"Forma de pagemento: {pagamento}")
    case 2:
        pagamento = "Cartão de crédito"
        acrescimo = comanda * 0.1
        acrescimo2 = comanda + (comanda * 0.1)
        print(f"\nValor total comanda {comanda}")
        print(f"Forma de pagemento: {pagamento}")
        print(f"Seu acrescimo foi de: {acrescimo}")
        print(f"Sua comanda deu no total: {acrescimo2} ")
        
print(f"Os pratos escolhidos foram:  {comida} ")
print(f"codigos dos pratos :{codigos_pratos}")





        