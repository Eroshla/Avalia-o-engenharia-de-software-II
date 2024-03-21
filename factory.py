from abc import ABC, abstractmethod

# Definindo a classe abstrata Transporte
class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass

# Definindo a classe Moto que herda da classe Transporte
class Moto(Transporte):
    def entregar(self, pedido: str):
        for i in range(5):
                tempo = 5 - i
                print("o pedido chegando, tempo para chegar: ", tempo ," minutos")
            
        print ("Entrega do pedido: ", pedido+ ". feita por moto")

# Definindo a classe Bicicleta que herda da classe Transporte
class Bicicleta(Transporte):
    def entregar(self, pedido: str):
        for i in range(10):
            tempo = 10 - i
            print("pedido chegando, tempo para chegar: ", tempo ," minutos")
            
        print ("Entrega do pedido: ", pedido+ ". feita por bicicleta")

# Definindo a classe abstrata Logistica
class Logistica(ABC):
    @abstractmethod
    def criar_transporte(self) -> Transporte:
        pass

    def planejar_entrega(self):
        # Chamando o método criar_transporte para obter um objeto de transporte
        transporte = self.criar_transporte()
        # Chamando o método entregar do objeto de transporte obtido
        return transporte.entregar()

# Definindo a classe LogisticaMoto que herda da classe Logistica
class LogisticaMoto(Logistica):
    def criar_transporte(self) -> Transporte:
        # Retornando um objeto da classe Moto
        return Moto()

# Definindo a classe LogisticaCiclista que herda da classe Logistica
class LogisticaCiclista(Logistica):
    def criar_transporte(self) -> Transporte:
        # Retornando um objeto da classe Bicicleta
        return Bicicleta()