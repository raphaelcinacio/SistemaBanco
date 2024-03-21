"""

Eu tenho uma PESSOAFISICA que é um CLIENTE
Eu tenho um CLIENTE e esse CLIENTE possui uma CONTA
Uma CONTA é do tipo CONTACORRENTE
Uma CONTA possui um HISTORICO

PESSOAFISICA >> CLIENTE >> CONTA >> CONTACORRENTE >> HISTORICO

No HISTORICO, registramos as ações de DEPOSITO E SAQUE, que implementam uma interface comum chamada TRANSACAO

As classes DEPOSITO e SAQUE, não são responsáveis por gerir a regra de negócio, mas sim por gerar registros no HISTORICO. A Classe TRANSACAO é reponsável
por garantir que as classes DEPOSITO e SAQUE tenham que implementar os mesmos métodos

"""
from Deposito import Deposito
from MenuApp import Menu
from ContaCorrente import ContaCorrente
from PessoaFisica import PessoaFisica
from Saque import Saque

contas = []


def buscar_cliente(cpf):
    conta_cliente = None
    cliente = None
    for conta in contas:
        if conta.to_dict().get("cliente").cpf == cpf:
            conta_cliente = conta
            cliente = conta.to_dict().get("cliente")
    return conta_cliente, cliente


def criar_conta(sequencial_conta):
    cpf = input("Informe seu cpf: ")
    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    endereco = input("Informe seu endereço: ")
    pessoa = PessoaFisica(cpf, nome, data_nascimento, endereco)
    conta = ContaCorrente.nova_conta_corrente(pessoa, sequencial_conta)
    contas.append(conta)


def exibir_historico(cpf):
    conta_cliente = buscar_cliente(cpf)

    if conta_cliente[0] is not None:
        for item in conta_cliente[0].historico.transacoes:
            print(item)
    else:
        print("Cliente não encontrado")


def executar_transacao(tipo, cpf):
    valores = buscar_cliente(cpf)
    conta_cliente = valores[0]
    cliente = valores[1]
    if tipo == 1:
        valor = float(input("Digite o valor do Saque: "))
        cliente.realizar_transacao(conta_cliente, Saque(valor))
    elif tipo == 2:
        valor = float(input("Digite o valor do Deposito: "))
        cliente.realizar_transacao(conta_cliente, Deposito(valor))
    else:
        print("Tipo de transação não cadastrada")


def main():
    sequencial_conta = 1
    while True:

        print(Menu.montar_menu())
        option = int(input("Digite a opção: "))

        match option:
            case 1:
                criar_conta(sequencial_conta)
                sequencial_conta += 1
            case 2:
                if len(contas) > 0:
                    cpf_busca = input("Digite o cpf: ")
                    exibir_historico(cpf_busca)
                else:
                    print("Não há conta criada")
            case 3:
                if len(contas) > 0:
                    cpf_busca = input("Digite o cpf: ")
                    resposta = int(input("Qual operação deseja realizar?\n1 - Saque\n2 - Deposito\n"))
                    executar_transacao(resposta, cpf_busca)
                else:
                    print("A conta não foi criada")

            case 4:
                print("\nFinalizando o app...")
                break
            case _:
                print("\nOpção inválida.")


main()
