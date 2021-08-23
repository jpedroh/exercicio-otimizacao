from math import exp, sqrt
from random import sample, random

DISTANCIAS = []

def construir_estado_inicial(cidades):
  return list(range(0, len(cidades)))

def calcular_temperatura(t):
  if(t <= 5):
    return 10
  elif t <= 9:
    return 5
  return 0

def escolher_sucessor(no_atual):
  return sample(no_atual, len(no_atual))

def calcular_valor(no):
  valor = 0
  for i in range(0, len(no) - 1):
    valor += DISTANCIAS[i][i+1]
  return valor

def probabilidade_aleatoria():
  return random()

def calcular_probabilidade_no(delta_e, T):
  return exp(delta_e/T)

def tempera_simulada(cidades):
  no_atual = construir_estado_inicial(cidades)
  t = 0

  while True:
    T = calcular_temperatura(t)
    
    if T == 0:
      return no_atual

    proximo_no = escolher_sucessor(no_atual)
    delta_e = calcular_valor(proximo_no) - calcular_valor(no_atual)

    if delta_e > 0:
      no_atual = proximo_no
    elif probabilidade_aleatoria() < calcular_probabilidade_no(delta_e, T):
      no_atual = proximo_no

    t += 1

    print(no_atual, calcular_valor(no_atual))

def calcular_distancia(a, b):
  return sqrt((float(a[0]) - float(b[0]))**2 + (float(a[1]) - float(b[1]))**2)

def calcular_distancias(arquivo):
  f = open(arquivo)
  linhas = [line.rstrip() for line in f]
  f.close()
  cidades = [city.split(' ') for city in linhas]

  for cidade in cidades:
    distancias = []

    for destino in cidades:
      distancias.append(calcular_distancia([cidade[1], cidade[2]], [destino[1], destino[2]]))
    DISTANCIAS.append(distancias)

if __name__ == "__main__":
  calcular_distancias("dj38.tsp")
  tempera_simulada(list(range(0, 38)))
