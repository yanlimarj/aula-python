from datetime import date
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

pessoa1 = Pessoa(cpf=12345678900, nome = "Raphael", nascimento = date(1984, 7, 26), oculos=True)

marca1 = Marca(id = 1, nome = "Fiat", sigla = "FIA")

veiculo1 = Veiculo(placa = "LRW1I27", cor = "Cinza", proprietario = pessoa1, marca = marca1)

