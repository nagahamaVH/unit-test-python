import convert_roman as cr
import pytest

@pytest.fixture
def known_values():
    known_values = ( (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (7, 'VII'),
    (8, 'VIII'),
    (9, 'IX'),
    (10, 'X'),
    (50, 'L'),
    (100, 'C'),
    (500, 'D'),
    (1000, 'M'),
    (31, 'XXXI'),
    (148, 'CXLVIII'),
    (294, 'CCXCIV'),
    (312, 'CCCXII'),
    (421, 'CDXXI'),
    (528, 'DXXVIII'),
    (621, 'DCXXI'),
    (782, 'DCCLXXXII'),
    (870, 'DCCCLXX'),
    (941, 'CMXLI'),
    (1043, 'MXLIII'),
    (1110, 'MCX'),
    (1226, 'MCCXXVI'),
    (1301, 'MCCCI'),
    (1485, 'MCDLXXXV'),
    (1509, 'MDIX'),
    (1607, 'MDCVII'),
    (1754, 'MDCCLIV'),
    (1832, 'MDCCCXXXII'),
    (1993, 'MCMXCIII'),
    (2074, 'MMLXXIV'),
    (2152, 'MMCLII'),
    (2212, 'MMCCXII'),
    (2343, 'MMCCCXLIII'),
    (2499, 'MMCDXCIX'),
    (2574, 'MMDLXXIV'),
    (2646, 'MMDCXLVI'),
    (2723, 'MMDCCXXIII'),
    (2892, 'MMDCCCXCII'),
    (2975, 'MMCMLXXV'),
    (3051, 'MMMLI'),
    (3185, 'MMMCLXXXV'),
    (3250, 'MMMCCL'),
    (3313, 'MMMCCCXIII'),
    (3408, 'MMMCDVIII'),
    (3501, 'MMMDI'),
    (3610, 'MMMDCX'),
    (3743, 'MMMDCCXLIII'),
    (3844, 'MMMDCCCXLIV'),
    (3888, 'MMMDCCCLXXXVIII'),
    (3940, 'MMMCMXL'),
    (3999, 'MMMCMXCIX'))

    return known_values

def test_if_algebraic_number_correspond_to_roman_number(known_values):
    '''o valor númerico de entrada deve ter um correspondente romano'''
    
    for integer, roman in known_values:
        converted_roman = cr.to_roman(integer)

        assert roman == converted_roman
