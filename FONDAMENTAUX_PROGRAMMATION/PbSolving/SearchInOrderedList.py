
def search_in_ordered_list(source, target):
    index_inf = 0
    index_sup = len(source) - 1

    while index_inf <= index_sup:
        index_test = (index_sup + index_inf) // 2

        if source[index_test] == target:
            return index_test
        elif source[index_test] > target:
            index_sup = index_test - 1
        else:
            index_inf = index_test + 1

    return -1


MyOrderedList = [2, 5, 7, 9, 14, 32, 33, 35, 40, 50, 60, 70, 80, 200, 400]
MyTarget = 0

IndexMyTarget = search_in_ordered_list(MyOrderedList, MyTarget)

if IndexMyTarget >= 0:
    print(MyTarget, '@Index :', IndexMyTarget, 'Check=', MyOrderedList[IndexMyTarget] == MyTarget)
else:
    print(MyTarget, 'Not found')
