
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

def moda(L, left, right):
    if left >= right:
        return None

    new_l = []
    for i in range(left, right + 1):
        new_l.append(L[i])

    new_l = quick_sort(new_l)
    right = (len(new_l))

    moda = None
    liczebnosc1 = 0
    i = left
    liczebnosc2 = 1

    for i in range(right - 1):
        if new_l[i] == new_l[i+1]:
            liczebnosc2 += 1
            # na biezaco uaktualniamy najlepszego kandydata
            if liczebnosc2 > liczebnosc1:  # jest lepszy kandydat
                liczebnosc1 = liczebnosc2
                moda = i
        else:
            liczebnosc2 = 1

    return new_l[moda]



