from menu import Menu
from datetime import datetime
import time
from atualiza_saldo import Atualiza_Saldo
from extrato import Extrato



class Deposito:
    numero_depositos = 0
        
    def operacao_de_deposito():
        
        deposito = float(input("Informe o valor que deseja depositar em sua conta: "))
        
        if deposito > 0:
            print("Estamos processando o seu depósito...")
            time.sleep(2)
            Atualiza_Saldo.atualizando_saldo(deposito, "deposito")
            Extrato.extrato += [f"Deposito de R${deposito: .2f}          {datetime.now()}"]
            print(Extrato.extrato)
            print(f"""
                                
                Agradecemos por usar nossos serviços.
                
                """)
        
        
        else:
            print("""
                Os valores para depósito devem ser positivos. 
                Se desejar efetuar um saque vá em  menu inicial e digite a opção [s].
                """)
            time.sleep(1)