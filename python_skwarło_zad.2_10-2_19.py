import random

#Zad.2.10

line = "mamy " \
       "dany " \
       "napis " \
       "wielowierszowy " \
       "zajmujacy " \
       "wiele " \
       "wierszy " \
	   "GvR" \
       
X = line.split()
print(len(X))

#Zad.2.11

word = "word"
print("_".join(word))

#Zad.2.12

first = ""
last = ""
for x in X:
    first = first + x[0]
    last = last + x[len(x)-1]

print(first)
print(last)

#Zad.2.13

Ln = []
for x in X:
    Ln.append(len(x))

print(sum(Ln))

#Zad.2.14

X.sort(key=len)
print(X[len(X)-1])
print(len(X[len(X)-1]))

#Zad.2.15

L = [3,4,6,11,7,50,1]
wrd = ""
for x in L:
    wrd += str(x)

print(wrd)

#Zad.2.16

print(line.replace("GvR","Guido van Rossum"))

#Zad.2.17

X.sort(key=len)
print(X)
X.sort()
print(X)

#Zad.2.18

c = 5614367101267
m = str(c)
print("0 występuje: ",m.count("0")," razy")
print("0 występuje na pozycji:",m.index("0"))

#Zad.2.19

L = [7,10,678,4,50,256,1,36,128,6,64,512]
newWord = ""
for x in range (4):
    p = str(random.choice(L))
    newWord += p.zfill(3)
    
print(newWord)








