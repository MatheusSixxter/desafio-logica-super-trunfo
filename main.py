import random

# Cartas disponíveis no jogo
cartas = [
    {"nome": "Carta A", "ataque": 80, "defesa": 60, "magia": 40},
    {"nome": "Carta B", "ataque": 70, "defesa": 90, "magia": 50},
    {"nome": "Carta C", "ataque": 60, "defesa": 40, "magia": 95},
    {"nome": "Carta D", "ataque": 50, "defesa": 70, "magia": 85},
    {"nome": "Carta E", "ataque": 90, "defesa": 55, "magia": 60},
    {"nome": "Carta F", "ataque": 65, "defesa": 75, "magia": 70}
]

# Função para escolher cartas aleatórias
def distribuir_cartas():
    embaralhadas = random.sample(cartas, 6)
    return embaralhadas[:3], embaralhadas[3:]

# Função para escolher atributo válido
def escolher_atributo():
    while True:
        atributo = input("Escolha um atributo para competir (ataque, defesa ou magia): ").lower()
        if atributo in ["ataque", "defesa", "magia"]:
            return atributo
        else:
            print("Atributo inválido. Tente novamente.")

# Função para jogar uma rodada
def jogar_rodada(carta_jogador, carta_cpu):
    print(f"\nSua carta: {carta_jogador}")
    print(f"Carta do oponente: {carta_cpu}")

    atributo = escolher_atributo()
    valor_jogador = carta_jogador[atributo]
    valor_cpu = carta_cpu[atributo]

    print(f"Seu {atributo}: {valor_jogador} vs {valor_cpu} do oponente")

    if valor_jogador > valor_cpu:
        print("Você venceu a rodada!")
        return 1
    elif valor_jogador < valor_cpu:
        print("Você perdeu a rodada.")
        return -1
    else:
        print("Empate.")
        return 0

# Início do jogo
print("=== Desafio Lógica Super Trunfo ===")
jogador_cartas, cpu_cartas = distribuir_cartas()
pontos = 0

for i in range(3):
    print(f"\n--- Rodada {i+1} ---")
    pontos += jogar_rodada(jogador_cartas[i], cpu_cartas[i])

# Resultado final
print("\n=== Resultado Final ===")
if pontos > 0:
    print("Parabéns! Você venceu a partida.")
elif pontos < 0:
    print("Você perdeu a partida.")
else:
    print("A partida terminou empatada.")
