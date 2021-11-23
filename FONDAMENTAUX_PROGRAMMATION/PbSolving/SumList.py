def sum_list(list_integer):
    sigma = 0

    index = 0
    while index < len(list_integer):
        sigma += list_integer[index]
        index += 1

    return sigma


def sum_odd_even_list(list_integer):
    sigma_even = 0
    sigma_odd = 0

    index = 0
    while index < len(list_integer):
        if list_integer[index] % 2 == 0:
            sigma_even += list_integer[index]
        else:
            sigma_odd += list_integer[index]
        index += 1

    return sigma_even, sigma_odd


def min_max_list(list_value):
    min_value = list_value[0]
    max_value = list_value[0]

    index = 1
    while index < len(list_integer):

        if list_value[index] > max_value:
            max_value = list_value[index]
        elif list_value[index] < min_value:
            min_value = list_value[index]

        index += 1

    return min_value, max_value


def max_step_in_list(list_value):
    max_step = list_value[1] - list_value[0]
    previous_value = list_value[1]

    index = 2
    while index < len(list_value):
        step = list_value[index] - previous_value

        if step > max_step:
            max_step = step

        previous_value = list_value[index]

        index += 1

    return max_step


def reverse_list(list_value):
    index_inf = 0
    index_sup = len(list_value) - 1

    while index_sup > index_inf:
        tmp = list_value[index_inf]
        list_value[index_inf] = list_value[index_sup]
        list_value[index_sup] = tmp

        index_inf += 1
        index_sup -= 1

    return list_value


















