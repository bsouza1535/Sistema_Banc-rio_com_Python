from cliente import Usuario

class Visualizar_Usuario:

    def visualiza():

        for cpf, valor in Usuario.usuarios.items():
            print(valor, Usuario.usuarios.items)