from fractions import Fraction
from mpmath import mp

mp.dps = 200


def error_in_fixed_point(value_to_convert, word_bit_size):
    BitStatus = []
    remainder = value_to_convert
    converted_value = Fraction(0, 1)
    bit_weight = Fraction(1, 1)
    bit_count = 0
    while bit_count < word_bit_size:
        bit_status = remainder // bit_weight
        BitStatus.append(bit_status)
        remainder %= bit_weight
        converted_value += bit_status * bit_weight
        print(bit_count, mp.convert(value_to_convert - converted_value), value_to_convert - converted_value )
        bit_weight /= Fraction(2, 1)
        bit_count += 1

    return BitStatus


print(error_in_fixed_point(Fraction(1, 10), 128))
