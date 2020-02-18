
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
    new_l = []
    for i in range(left,right+1):
        new_l.append(L[i])

    new_l = quick_sort(new_l)
    right = (len(new_l))

    if right%2 != 0:
        srodek = right//2
        mediana = new_l[srodek]
        return mediana
    else:
        srodek = right/2
        mediana = (float(new_l[srodek - 1]+new_l[srodek]))/2
        return mediana




