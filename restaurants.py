class Restaurantes:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, nome, comida1, comida2, comida3):
        self.nome = nome
        self.comida1 = comida1
        self.comida2 = comida2
        self.comida3 = comida3

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_comida1(self):
        return self.comida1

    def set_comida1(self, comida1):
        self.comida1 = comida1

    def get_comida2(self):
        return self.comida2

    def set_comida2(self, comida2):
        self.comida2 = comida2

    def get_comida3(self):
        return self.comida3

    def set_comida3(self, comida3):
        self.comida3 = comida3

    def listar_comidas(self):
        print("Escolha uma comida:")
        print("1. " + self.comida1)
        print("2. " + self.comida2)
        print("3. " + self.comida3)
        
        escolha = input("Digite o número da comida desejada (1, 2 ou 3): ")
        
        if escolha == "1":
            for i in range(5):
                print("verificando pagamento....")
            print("Pagamento aprovado, pedido confirmado")
            return self.comida1
        elif escolha == "2":
            for i in range(5):
                print("verificando pagamento....")
            print("Pagamento aprovado, pedido confirmado")
            return self.comida2
        elif escolha == "3":
            for i in range(5):
                print("verificando pagamento....")
            print("Pagamento aprovado, pedido confirmado")
            return self.comida3
        else:
            return "Opção inválida. Por favor, escolha um número válido."
    def receber_avaliacao(self, estrelas):
        print("Obrigado pela avaliação de ",estrelas, "estrelas.")