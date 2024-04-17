from atualiza_saldo import Atualiza_Saldo

class Extrato:

    extrato = []

    def operacao_de_extrato():
        
        print("========== EXTRATO ==========")
        for i in Extrato.extrato:
            print(i)
        print("=============================")
        print("=========SALDO TOTAL=========")
        print("         R$",  Atualiza_Saldo.saldo)