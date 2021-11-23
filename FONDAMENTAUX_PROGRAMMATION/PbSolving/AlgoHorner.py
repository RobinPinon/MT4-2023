def string2int(num_string):
    dec_value = 0
    for current_char in num_string:
        dec_value *= 10
        dec_value += ord(current_char) - ord("0")

    return dec_value


def string2int_trivial(num_string):
    column_weight = 1
    dec_value = 0

    char_index = len(num_string) - 1
    while char_index >= 0:
        column_value = ord(num_string[char_index]) - ord("0")
        dec_value += column_value * column_weight
        column_weight *= 10
        char_index -= 1

    return dec_value


def string2intV2(num_string):
    dec_value = 0
    char_index = 0
    while char_index < len(num_string):
        dec_value *= 10
        dec_value += ord(num_string[char_index]) - ord("0")
        char_index += 1

    return dec_value


decimal_string = "1048576"

print(string2int(decimal_string))
print(string2int_trivial(decimal_string))
print(string2intV2(decimal_string))