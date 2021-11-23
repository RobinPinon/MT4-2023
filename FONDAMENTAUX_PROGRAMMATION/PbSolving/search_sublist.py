def search_sub_list(source, target):

    len_source = len(source)
    len_target = len(target)

    index_source = 0
    while index_source <= (len_source - len_target):

        index_target = 0
        index_test = index_source
        while index_target < len_target and target[index_target] == source[index_test]:
            index_target += 1
            index_test += 1

        if index_target == len_target:
            return index_source

        index_source += 1

    return -1

MyList = [12, 54, 76, 87, 11, 32, 17, 87, 99, 102]
MytrgList = [32, 17, 87, 99, 102]

print(search_sub_list(MyList, MytrgList))




















