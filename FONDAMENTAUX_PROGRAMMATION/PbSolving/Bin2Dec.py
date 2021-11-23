def bin2dec(binary_list):
    dec_value = 0
    for current_bit in binary_list:
        dec_value <<= 1
        dec_value += current_bit

    return dec_value


def bin2dec_trivial(binary_list):
    column_weight = 1
    dec_value = 0

    bit_index = len(binary_list) - 1
    while bit_index >= 0:
        column_value = binary_list[bit_index]
        dec_value += column_value * column_weight
        column_weight <<= 1

        bit_index -= 1

    return dec_value


binary_list = [1, 1, 1, 1, 1, 1, 1, 0]

print(bin2dec(binary_list))
print(bin2dec_trivial(binary_list))
