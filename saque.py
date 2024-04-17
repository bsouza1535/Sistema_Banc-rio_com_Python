from atualiza_saldo import Atualiza_Saldo
from datetime import datetime
import time
from extrato import Extrato

class Operacao_Saque:

    def operacao_de_saque():

        numero_saques = 0
        LIMITE_SAQUES = 3
        
        
        valor_saque = float(input("Digite aqui o valor que deseja sacar de sua conta: "))
        
        if 0 <= numero_saques < LIMITE_SAQUES and  0 < valor_saque <= 500 and Atualiza_Saldo.saldo >= valor_saque:
            print("Estamos efetuando o seu saque...")
            time.sleep(1)
            Atualiza_Saldo.atualizando_saldo(valor_saque, "saque")
            Extrato.extrato += [f"Saque de R${valor_saque: .2f}          {datetime.now()}"]
            numero_saques += 1
            print(f"""
                Agradecemos por usar nossos serviços.
                """)
        
        elif Atualiza_Saldo.saldo <= 0:
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

