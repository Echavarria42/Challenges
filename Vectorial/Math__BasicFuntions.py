def subtraction(lst):
    inicio = lst[0]
    for i in lst[1:]: 
        inicio -= i
    return inicio

def multiplication(lst):
    solution = 1
    for i in lst:
        solution *= i
    return solution

def division(lst):
    inicio = lst[0]
    for i in lst[1:]: 
        inicio /= i
    return inicio

def raising(lst):
    inicio = lst[0]
    for i in lst[1:]: 
        inicio **= i
    return inicio

def root(lst):
    inicio = lst[0]
    return inicio**(1/(multiplication(lst[1:])))

#Let "X" be a list to be inserted and "i" be the index where you want it to be inserted.
def insert(x, lst, i):
    conj =  lst[:i] + [x] + lst[i:]
    sol = ""
    for i in conj:
        sol += str(i)
    print(sol)
    return conj

#insert an item into a list at all its initial indices
def insert_multiple(x, lst):
    solution = []
    for i in range(len(lst)+1):
        num_new = insert(x, lst, i)
        solution.append(num_new)
    return solution

def swap(c):
    if len(c) == 0:
        return [[]]
    return sum([insert_multiple(c[0], s)
                for s in insert(c[1:])],
               [])

def average(lista):
    return sum(lista)/len(lista)



