def dec2bin(dec_value):
    binary_value = [dec_value & 1]
    dec_value >>= 1

    while dec_value > 0:
        binary_value.insert(0, dec_value & 1)
        dec_value >>= 1

    return binary_value


print(dec2bin(12))
