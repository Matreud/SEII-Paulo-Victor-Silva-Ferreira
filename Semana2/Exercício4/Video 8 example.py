
# Numero de dias por mês, primeiro valor placeholder
dias_do_mês = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def é_bissexto(ano):
    """Retorna True para anos bisextos, False caso contrário."""

    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


def dias_no_mês(ano, mês):
    """Retorna o número de dias naquele mês daquele ano."""

    # ano 2017
    # mês 2
    if not 1 <= mês <= 12:
        return 'Mês inválido'

    if mês == 2 and é_bissexto(ano):
        return 29

    return dias_do_mês[mês]

print(dias_no_mês(2017, 2))