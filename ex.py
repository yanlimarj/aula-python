from banco import BancoDeDados
from datetime import date
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo


if __name__ == '__main__':
    
    banco = BancoDeDados() 
    banco.conectar()
    banco.criar_tabelas()
    
    pessoa1 = Pessoa(cpf=12345678900, nome = "Raphael", nascimento = date(1984, 7, 26), oculos=True)
    banco.inserir_pessoa(pessoa1)
    
    marca1 = Marca(id = 1, nome = "FIAT", sigla = "FIA")
    banco.inserir_marca(marca1)
    
    veiculo1 = Veiculo(placa = "LRW1I27", cor = "Cinza", proprietario = pessoa1, marca = marca1)
    banco.inserir_veiculo(veiculo1)
    
    print("Pessoas:")
    for pessoa in banco.buscar_todas_pessoas():
        print(pessoa)
       
    print("\nMarcas:")
    for marca in banco.buscar_todas_marcas():
        print(marca)
        
    print("\nVeículos:")
    for veiculo in banco.buscar_todos_veiculos():
        print(veiculo)
        
    banco.fechar_conexao()