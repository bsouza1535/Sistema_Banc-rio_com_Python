

class Atualiza_Saldo:

    saldo = 0


    def atualizando_saldo(valor, operacao):
        
        if operacao == "deposito":
            Atualiza_Saldo.saldo += valor
            
        elif operacao == "saque":
            Atualiza_Saldo.saldo -= valor