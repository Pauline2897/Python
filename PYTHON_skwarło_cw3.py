#Zad.3.1. czy podany kod jest poprawny składniowo w Pythonie

x = 2 ; y = 3 ; #bez średników x,y = 2,3
if (x > y):
    result = x; #nie powinno być średnika
else:
    result = y; #nie powinno być średnika
	
for i in "qwerty": if ord(i) < 100: print i // powinno być print(i)
for i in "axby": print ord(i) if ord(i) < 100 else i // powinno być print(ord(i) if ord(i)<100 else i)

#Zad.3.2.co jest złego w kodzie

L = [3, 5, 4] ; L = L.sort()

x, y = 1, 2, 3 # przypisywane są 3 wartości do dwóch zmiennych

X = 1, 2, 3 ; X[1] = 4 # x nie jest listą

X = [1, 2, 3] ; X[3] = 4 #Listy nie można rozszerzać w ten sposób

X = "abc" ; X.append("d") # String jest traktowany jako lista

map(pow, range(8)) # pow() - potrzebuje dwóch argumentów

#Zad.3.3 Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.

for x in range (31):
    if (x%3!=0):
	    print x
		
#Zad.3.4.Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący parę x i trzecią potęgę x. 
#Zatrzymanie programu następuje po wpisaniu z klawiatury stop. 
#Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

while true:
    reply = raw_input("Podaj liczbę float: ")
    if reply == "stop":
        break
    elif not reply.isdigit():
        print "To nie jest liczba"
    else:
        print float (reply), float (reply) ** 3
		
#Zad.3.5.Napisać program rysujący "miarkę" o zadanej długości. 
#Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). 
#Należy zbudować pełny string, a potem go wypisać.

print("int %d float %f str %s" % (5, 3.14159, "napis"))
print("%-10s %-10s" % ("napis1", "napis2"))

length = 15
pattern = "|...."
linear = [' ', '0']
for i in range(length):
    linear[0] += pattern
    linear[1] += "%5s" % (i + 1)
print(linear[0], '\n', linear[1])

#Zad.3.6.Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać. 

row = "+---"
column = "|   "
SIZE = 5
board = ''


def generate_el(pattern, end_cap):
    board = ''
    for j in range(SIZE):
        board += pattern
        if j == SIZE - 1:
            board += end_cap + '\n'
    return board


for _ in range(SIZE):
    board += generate_el(row, '+')
    board += generate_el(column, '|')
board += generate_el(row, '+')
print(board)

#Zad 3.8.Dla dwóch sekwencji znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń), 
#(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

b = [(0, 3, 4, 9), (1, 2), (5, 12, 7)]
a = [[3, 4, 9], (13, 2), [7, 8], (0, 6, 11)]
new_a = set()
new_b = set()

for el in a:
    new_a.update(set(el))
print(new_a)

for el in b:
    new_b.update(set(el))
print(new_b)

print(new_a.intersection(new_b))
print(new_a.union(new_b))

#Zad.3.9. Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. 
#Znaleźć listę zawierającą sumy liczb z tych sekwencji. Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].

elements = [[], [1, 2, 3], (10, 15), [7, 8], (4, 5, 6)]
print(list(map(lambda x: sum(x), elements)))

#Zad.3.10.Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie

D = {}
D[I]= 1
D[V]= 5
D[X]=10
D[L]=50
D[C]=100
D[D]=500
D[M]=1000

#inne sposoby

D={I:1, V:5, X:10, L:50, C:100, D:500, M:1000}

D= dict([(I,1),(V,5),(X,10),(L,50),(C,100),(D,500),(M,1000)])

