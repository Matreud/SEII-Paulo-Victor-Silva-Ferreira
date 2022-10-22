print('my_module importado...')

teste = 'String teste'


def encontrar_index(para_procura, alvo):
    '''Encontra o index de um valor em uma sequencia'''
    for i, value in enumerate(para_procura):
        if value == alvo:
            return i

    return -1