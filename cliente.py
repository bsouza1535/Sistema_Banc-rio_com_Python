

class Usuario:
    usuarios = {}

    def cadastro():
        
        print("=== Cadastro de Clientes ===")
        cpf = input("Digite o CPF do cliente: ")
        nome = input("Digite o nome do Cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        email = input("Digite aqui o email do cliente: ")
        sexo = input("Digite o sexo do cliente: ")
        conta = input("Qual o número da conta do cliente: ")
        
        # Adicionando o usuário ao dicionário de usuários
        Usuario.usuarios[cpf] = {"Nome:": nome, "Telefone:": telefone, "Email:": email, "Sexo:": sexo, "Conta:": conta}

        return Usuario.usuarios
        
        print("Usuário cadastrado com sucesso!")


