import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# from src.models import Cliente

MENOR_IDADE = 18
CARACTERE_OBRIGATORIA = "@"
TAMANHO_MINIMO_NOME = 3


class CadastroCliente:
    def __init__(self):
        self.clientes_cadastrados = []

    def cadastrar_cliente(self, cliente):

        if cliente.idade < MENOR_IDADE:
            return "Cliente menor de idadde, não cadastrado"

        if not CARACTERE_OBRIGATORIA in cliente.email:
            return "Email invalido, não cadastrado"

        if len(cliente.nome) < TAMANHO_MINIMO_NOME:
            return "Nome invalido, não cadastrado"

        self.clientes_cadastrados.append(cliente)

        if len(self.clientes_cadastrados) > 0:
            return "Cadastrado com sucesso"
