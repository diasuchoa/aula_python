import sys
sys.path.append(".")

from src.models.Cliente import Cliente
from src.controlers.CadastroCliente import CadastroCliente


def test_que_cliente_seja_cadastrado_com_sucesso():
    cliente = Cliente("junior", 39, "junior@email.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cadastrado com sucesso" == resposta


def test_que_cliente_nao_pode_ser_menor_idade():
    cliente = Cliente("junior", 16, "junior@email.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cliente menor de idadde, não cadastrado" == resposta


def test_que_email_valido():
    cliente = Cliente("junior", 39, "juniormail.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Email invalido, não cadastrado" == resposta


def test_nome_deve_ser_maior_que_tres_caracteres():
    cliente = Cliente("ju", 39, "junior@mail.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Nome invalido, não cadastrado" == resposta
