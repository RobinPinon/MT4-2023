# --------------------------- Fonction Classique ---------------------------
def string2int(string):
    int_return = int(0)

    for chars in string:
        int_return *= 10
        int_return += ord(chars) - ord('0')

    return int_return


def bin2dec(binary_list):
    dec_value = 0
    for current_bit in binary_list:
        # dec_value <<= 1
        dec_value *= 2
        dec_value += current_bit

    return dec_value


# --------------------------- Fonction Trivial ---------------------------
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


def bin2dec_trivial(binary_list):
    column_weight = 1
    dec_value = 0

    bit_index = len(binary_list) - 1
    while bit_index >= 0:
        column_value = binary_list[bit_index]
        dec_value += column_value * column_weight
        column_weight *=2
        bit_index -= 1

    return dec_value


# --------------------------- Affichage classique ---------------------------
print(string2int('1982'))

print(bin2dec([1, 0, 1, 1]))

# --------------------------- Affichage trivial ---------------------------
decimal_string = "1982"
print(string2int_trivial(decimal_string))

print(bin2dec_trivial([1, 0, 1, 1]))


