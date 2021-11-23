def bin2dec(binary_list):
    dec_value = 0
    for current_bit in binary_list:
        dec_value <<= 1
        dec_value += current_bit

    return dec_value


def one_bit_add(bit_a, bit_b, carry_in):
    s_xor1 = bit_a ^ bit_b
    s = s_xor1 ^ carry_in

    s_and_1 = s_xor1 & carry_in
    s_and_2 = bit_a & bit_b

    carry_out = s_and_1 | s_and_2

    return s, carry_out


def add_binary_word(word_a, word_b):
    binary_sum = []
    carry = 0

    bit_index = len(word_a) - 1
    while bit_index >= 0:
        [bit_sum, carry] = one_bit_add(word_a[bit_index], word_b[bit_index], carry)

        binary_sum.insert(0, bit_sum)
        bit_index -= 1

    if carry == 1 :
        binary_sum.insert(0,carry)

    return binary_sum


A = [1, 1, 0, 1]
B = [1, 0, 1, 1]

print("A=", A, bin2dec(A))
print("B=", B, bin2dec(B))

add_value = add_binary_word(A, B)

print("Sum", add_value, bin2dec(add_value))
