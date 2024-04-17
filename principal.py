import time
from datetime import datetime
from menu import Menu
from deposito import Deposito
from atualiza_saldo import Atualiza_Saldo
from saque import Operacao_Saque
from extrato import Extrato
from cliente import Usuario
from visualiza_usuario import Visualizar_Usuario
 
limite = 500

class Main:

    def main():
        
        while True:
            
            opcao = input(Menu.menu)
            
            if opcao == "d":
                time.sleep(1)
                Deposito.operacao_de_deposito()
            
            elif opcao == "s":
                time.sleep(1)
                Operacao_Saque.operacao_de_saque()
                
            elif opcao == "e":
                Extrato.operacao_de_extrato()
                
            elif opcao == "c":
                Usuario.cadastro()
            
            elif opcao == "v":
                Visualizar_Usuario.visualiza()
                
            elif opcao == "q":
                break
            
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

Main.main()