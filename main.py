import time
from datetime import datetime


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUES = 3

def atualizando_saldo(valor, operacao):
    
    global saldo
    
    if operacao == "deposito":
        saldo += valor
        
    elif operacao == "saque":
        saldo -= valor
    
        
def operacao_de_deposito():
    
    global numero_depositos, extrato
    
    deposito = float(input("Informe o valor que deseja depositar em sua conta: "))
    
    if deposito > 0:
        print("Estamos processando o seu depósito...")
        time.sleep(2)
        atualizando_saldo(deposito, "deposito")
        extrato += [f"Deposito de R${deposito: .2f}          {datetime.now()}"]
        print(extrato)
        print(f"""
                            
            Agradecemos por usar nossos serviços.
              
              """)
    
    
    else:
        print("""
              Os valores para depósito devem ser positivos. 
              Se desejar efetuar um saque vá em  menu inicial e digite a opção [s].
              """)
        time.sleep(1)


def operacao_de_saque():
    
    global numero_saques, LIMITE_SAQUES, saldo, extrato
    
    valor_saque = float(input("Digite aqui o valor que deseja sacar de sua conta: "))
    
    if 0 <= numero_saques < LIMITE_SAQUES and  0 < valor_saque <= 500 and saldo >= valor_saque:
        print("Estamos efetuando o seu saque...")
        time.sleep(1)
        atualizando_saldo(valor_saque, "saque")
        extrato += [f"Saque de R${valor_saque: .2f}          {datetime.now()}"]
        numero_saques += 1
        print(f"""
              Agradecemos por usar nossos serviços.
              """)
    
    elif saldo <= 0:
        print("""Não é possível completar o processo pois você não tem saldo suficiente em conta para debitarmos a solicitação. """)
        
    elif valor_saque <= 0:
        print("O valor digitado não está correto. Digite um valor positivo se deseja continuar a operação. ")
        
    elif numero_saques >= LIMITE_SAQUES:
        print("""
              Limite diário de saque foi excedido. Por favor, tente novamente amanhã. 
              Lembramos que o seu limite diário de saque é de três saques.
              """)
    
    else:
        print("Operação inválida!! O valor especificado é maior que o limite de R$500,00 por saque...")


def operacao_de_extrato():
    
    global extrato, saldo
    
    print("========== EXTRATO ==========")
    for i in extrato:
        print(i)
    print("=============================")
              
             
    #print(f"""
    #      Segue o seu extrato:
          
    #      {extrato}
          
    #      """)
    

def main():
    
    while True:
        
        opcao = input(menu)
        
        if opcao == "d":
            time.sleep(1)
            operacao_de_deposito()
        
        elif opcao == "s":
            time.sleep(1)
            operacao_de_saque()
            
        elif opcao == "e":
            operacao_de_extrato()
            
        elif opcao == "q":
            break
        
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
 
main()