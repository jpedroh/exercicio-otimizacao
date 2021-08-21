def construir_estado_inicial(cidades):
  pass

def calcular_temperatura(t):
  pass

def escolher_sucessor(no_atual):
  pass

def calcular_valor(no):
  pass

def probabilidade_aleatoria():
  pass

def calcular_probabilidade_no(delta_e, T):
  pass

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

if __name__ == "__main__":
    tempera_simulada([])