def cmp_str(string_a, string_b) :
    index_char = 0
    while index_char<len(string_a) :
        if string_a[index_char] != string_b[index_char] :
            return False
        index_char += 1
    return True


print(cmp_str('DALBERA', 'DALBERA'))
print(cmp_str('DaLBERA', 'DALBERA'))
