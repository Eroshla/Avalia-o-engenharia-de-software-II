from restaurants import Restaurantes
import factory
import random


restaurante1 = Restaurantes('japones', 'combo salmão', 'combo atum', 'combo misto')
restaurante2 = Restaurantes('Segredos da vovó', 'pão', 'pão de queijo', 'triangulo')

logistica_moto = factory.LogisticaMoto()
logistica_ciclista = factory.LogisticaCiclista()

moto = logistica_moto.criar_transporte()
bicicleta = logistica_ciclista.criar_transporte()

def selecionar_restaurante():
    print ("Escolha um restaurante:")
    opcao = int(input("1. Japones\n2. Segredos da vovó\n"))
    if opcao == 1: return restaurante1 
    elif opcao == 2: return restaurante2 
    else: return None

def selecionar_numero():
    return random.randint(1, 2)

numero_selecionado = selecionar_numero()

restaurante_selecionado = selecionar_restaurante()
comida = restaurante_selecionado.listar_comidas()

veiculo_entrega = selecionar_numero()

if veiculo_entrega == 1:
    moto.entregar(comida)
elif veiculo_entrega == 2:
    bicicleta.entregar(comida)
    
avaliação = input("Avalie o pedido: ")

restaurante_selecionado.receber_avaliacao(avaliação)