def heapify(customList, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and customList[l] < customList[smallest]:
        smallest = l
    if r < n and customList[r] < customList[smallest]:
        smallest = r
    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)


def heapSort(custom_list):
    n = len(custom_list)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(custom_list, n, i)
    for i in range(n - 1, 0, -1):
        custom_list[i], custom_list[0] = custom_list[0], custom_list[i]
        heapify(custom_list, i, 0)
    custom_list.reverse()
    return custom_list


ex = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(heapSort(ex))
