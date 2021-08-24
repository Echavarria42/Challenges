def suma(lst):
    return sum(lst)

def resta(lst):
    inicio = lst[0]
    for i in lst[1:]: 
        inicio -= i
    return inicio

def multiplicar(lst):
    solution = 1
    for i in lst:
        solution *= i
    return solution

def dividir(lst):
    inicio = lst[0]
    for i in lst[1:]: 
        inicio /= i
    return inicio

def elevar(lst):
    inicio = lst[0]
    for i in lst[1:]: 
        inicio **= i
    return inicio

def raiz(lst):
    inicio = lst[0]
    return inicio**(1/(multiplicar(lst[1:])))

def inserta(x, lst, i):
    conj =  lst[:i] + [x] + lst[i:]
    sol = ""
    for i in conj:
        sol += str(i)
    print(sol)
    return conj

def inserta_multiple(x, lst):
    solution = []
    for i in range(len(lst)+1):
        num_new = inserta(x, lst, i)
        solution.append(num_new)
    return solution

def permuta(c):
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s)
                for s in permuta(c[1:])],
               [])

def promedio(lista):
    return sum(lista)/len(lista)

def piramide(n):
    for i in range(n):
        print(" "*(n-i-1), end="")
        print(f"* "*(i+1))

print(piramide(5))