#Zad.4.2.Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return.

def get_linear(length=1):
    pattern = "....|"
    linear = ['|', '0']
    linear[0] += pattern * (length - 1)
    for i in range(1, length):
        linear[1] += "%5s" % i
    return str.join('\n', (linear[0], linear[1]))


def get_board(size=5):
    def generate_el(pattern, end_cap):
        board = pattern * size
        board += end_cap + '\n'
        return board

    row = "+---"
    column = "|   "
    board = ''
    for _ in range(size):
        board += generate_el(row, '+')
        board += generate_el(column, '|')
    board += generate_el(row, '+')
    return board


print(get_linear(length=15))
print(get_board(size=5))

#Zad.4.3.Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def get_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


print(get_factorial(5))

#Zad.4.4.Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

def fibonacci(n):
    a, b = 1, 1
    i = 0
    while i < n-1:
        a, b = b, a + b
        i += 1
    return a

print(fibonacci(6))

#Zad.4.5.Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie. 
#Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

def iter_reverse(L, left, right):
    assert left in range(len(L)) and left in range(len(L))
    if right < left:
        left, right = right, left
    for i in range((right - left) // 2):
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def replace(L, left, right):
    L[left], L[right] = L[right], L[left]
    if left < right:
        return replace(L, left + 1, right - 1)
    else:
        return True


L = [1, 2, 3, 4, 5, 6, 7, 8]
left = 1
right = 5
print(L)
iter_reverse(L, left, right)
print(L)
replace(L, left, right)
print(L)

#Zad.4.6.Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje. 

sequence = [(0, 1), 2, (6, [9, 12], (7, 4, (5, 3, 8)))]


def sum_seq(sequence):
    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum += sum_seq(item)
        else:
            sum += item
    return sum

print(sum_seq(sequence))

#Zad.4.7.Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. 
#Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji.

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print flatten(seq)            # [1,2,3,4,5,6,7,8,9]
"""
print("Zadanie 4.7:")
def flatten(sequence):
    L = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            L.extend(flatten(item))
        else:
            L.append(item)
    return L

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(sequence))