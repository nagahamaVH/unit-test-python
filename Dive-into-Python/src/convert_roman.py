# Mapa dos limites numericos para conversao
limit_numbers_map = ((1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'))

def to_roman(number):
    converted_roman = ''

    if not 0 < number < 4000:
        raise ValueError('Número invalido (deve estar entre 1 e 3999)')

    if not isinstance(number, int):
        raise ValueError('Número invalido (valor não inteiro não pode ser convertido)')

    for algebraic, roman in limit_numbers_map:
        while number >= algebraic:
            converted_roman += roman
            number -= algebraic
    
    return converted_roman

def from_roman(integer):
    pass

