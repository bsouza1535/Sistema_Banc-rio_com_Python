# Sistema_Banc-rio_com_Python

### Description:

Projeto indicado pela [DIO](https://web.dio.me/home) no bootcamp [Potência Tech powered by iFood | Ciência de Dados](https://web.dio.me/track/potencia-tech-powered-ifood-ciencias-de-dados-com-python).
Neste projeto, a intensão é criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Na simulação, essa seria a V1 do código o qual não necessita de questões avançadas, mas apenas as três operações de forma bem consisa. Na fase dois do código, pudemos implementar a funcionalidade de cadastros de clientes e a reorganização das funções em classes.
Segue a fio...

### Operação de depósito

Deve ser póssível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em indentificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação extrato:

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$xxx.xx, exemplo:
155.45 = R$1500.45

### Classes e cadastros

O sistema deve permitir que sejam cadastrados clientes e atrelado um número de conta para ele. Ademais, o código foi reestruturado para que cada funcionalidade tenha sua própria classe, ajudando na leitura e manutenção do código.
