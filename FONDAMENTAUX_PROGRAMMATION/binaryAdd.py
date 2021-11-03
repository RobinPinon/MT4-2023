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

    binary_sum.insert(0, carry)

    return binary_sum


print(one_bit_add(1, 1, 1))


A = [1, 0, 0, 1]
B = [1, 0, 1, 1]
print(add_binary_word(A, B))