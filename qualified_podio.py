# def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
#     lista = [] # Implemente aqui a lógica da função
#     lista.append(tempo_chegada1)
#     lista.append(tempo_chegada2)
#     lista.append(tempo_chegada3)
#     lista.sort()
#     variavel_de_retorno = f'1 - {lista[0]} minutos\n2 - {lista[1]} minutos\n3 - {lista[2]} minutos\n'
#     return variavel_de_retorno

# podio_olimpico(3,1,2

def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
    # Implemente aqui a lógica da função
    lista1 = []
    lista1.append(nome_corredor1)
    lista1.append(nome_corredor2)
    lista1.append(nome_corredor3)
    lista2 = []
    lista2.append(tempo_chegada1)
    lista2.append(tempo_chegada2)
    lista2.append(tempo_chegada3)
    lista1.sort()
    lista2.sort()
    variavel_de_retorno = f'1 - {lista1[0]} - {lista2[0]} minutos\n2 - {lista1[1]} - {lista2[1]}  minutos\n3 - {lista1[2]} - {lista2[2]}  minutos\n'
    return variavel_de_retorno