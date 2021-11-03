def string2int(string):
    int_return = int(0)

    for chars in string:
        # Axe d'amélioration
        # int_return *= 10
        # int_return += ord(chars) - ord('0')

        int_return = int_return*10 + ord(chars) - ord('0')

    return int_return


print(string2int('1982'))


def string2int_trivial(num_string):
    char_index = len(num_string) - 1
    column_weight = 1
    dec_value = 0
    while char_index >= 0:
        column_value = ord(num_string[char_index]) - ord("0")
        dec_value += column_value * column_weight
        column_weight *= 10
        char_index -= 1

    return dec_value


decimal_string = "12"

print(string2int_trivial(decimal_string))
