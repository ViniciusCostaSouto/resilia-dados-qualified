def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    lista = [] # Implemente aqui a lógica da função
    lista.append(tempo_chegada1)
    lista.append(tempo_chegada2)
    lista.append(tempo_chegada3)
    lista.sort()
    variavel_de_retorno = f'1 - {lista[0]} minutos\n2 - {lista[1]} minutos\n3 - {lista[2]} minutos\n'
    return variavel_de_retorno