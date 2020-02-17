
def quick_sort(L):


    if len(L) <= 1:
        return L
    # pobieranie pivota wg ktorego bedzimey operowac
    pivot = L[0]
    less = []

    # wszystkie mniejsze elementy od pivot przerzucamy do listy mniejszych
    for x in L:
        if x < pivot:
            less.append(x)

    # wszystkie rowne elementy przerzucamy do listy rownych
    equal = []
    for x in L:
        if x == pivot:
            equal.append(x)

    # wszystkie wiesze elementy od pivot przerzucamy do listy wiekszych
    greater = []
    for x in L:
        if x > pivot:
            greater.append(x)

    # (rekurencja) odnawiamy procedure dla mniejszych i wiekszych elementow
    return quick_sort(less) + equal + quick_sort(greater)


def mediana_sort(L, left, right):
    if left >= right:
        return None
    L = quick_sort(L)
    if right%2 != 0:
        srodek = right//2
        mediana = L[srodek]
        return mediana
    else:
        srodek = right/2
        mediana = (L[srodek - 1]+ L[srodek])/2
        return mediana

