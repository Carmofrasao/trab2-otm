#!/usr/bin/python3

import sys
import datetime as dt

ator = {
    'valor' :   0,
    'n_grupos': 0,
    'grupos':   [],
}

# Vetor com todos os atores disponiveis
Atores_disponiveis = []


if __name__ == "__main__":
    f = o = a = 0

    # Indentificando flags para a execução do Branch & Bound
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == '-f':
                f = 1
            elif sys.argv[i] == '-o':
                o = 1
            elif sys.argv[i] == '-a':
                a =1
    
    # -f = desligar os cortes de viabilidade
    # -o = desligar os cortes de otimalidade
    # -a = usar a função limitante dada pelos professores

    # Lendo numero de representações, atores e papeis 
    entrada = [int(x) for x in sys.stdin.read().split()]
    l = entrada[0] # numero de grupos sociais
    m = entrada[1] # numero de atores
    n = entrada[2] # numero de personagens
    # l = |S|, m = |A| e n = |P| 

    cursor = 3

    # Dados um conjunto S de grupos, um conjunto A de atores, um conjunto
    # P de personagens, e, para cada ator a ∈ A, um conjunto, Sa ⊆ S indicando os
    # grupos dos quais a faz parte, devemos encontrar um elenco que tenha um ator
    # para cada personagem (todos os atores podem fazer todas as personagens) e
    # todos os grupos tenham um representante. Além disso, também temos um
    # valor, va, associado com cada ator a ∈ A, e queremos que o custo do elenco
    # seja mínimo.
    # Ou seja, devemos encontrar um subconjunto X ⊆ A tal que:
    # - |X| = |P|;
    # - (UNIÃO)(a∈X)Sa = S; e
    # - (SOMATÓRIO)(a∈X)va seja mínimo.

    # Lendo atores e suas caracteristicas
    for _ in range(m):
        ator['valor'] = entrada[cursor]
        ator['n_grupos'] = entrada[cursor+1]
        for i in range(ator['n_grupos']):
            ator['grupos'].append(entrada[cursor+2+i])
        cursor += ator['n_grupos']+2
        aux = ator.copy()
        Atores_disponiveis.append(aux)
        ator['grupos'] = []

    # ------------------------CODIGO PRINCIPAL AQUI-------------------------------

    tempo_inicio = dt.datetime.now()

    tempo_total = dt.datetime.now() - tempo_inicio

    # ----------------------------------------------------------------------------