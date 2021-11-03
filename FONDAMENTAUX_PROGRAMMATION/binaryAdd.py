def one_bit_add(bit_a, bit_b, carry_in):

    s_xor1 = bit_a ^ bit_b
    s = s_xor1 ^ carry_in

    s_and_1 = s_xor1 & carry_in
    s_and_2 = bit_a & bit_b

    carry_out = s_and_1 | s_and_2

    return s, carry_out


print(one_bit_add(1, 1, 1,))
