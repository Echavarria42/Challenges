# ***ENCUENTRA LOS DIVISORES EXACTOS***


def Divisor(objetivo):
    lista = [i for i in range(2,objetivo) if objetivo % i == 0]
    if not lista:
        objetivo = str(objetivo)
        return f'{objetivo} is prime'
    else:
        return lista

print(Divisor(int(input('Dime un número: '))))

"""# ***ELEVA CADA DIGITO DE UN NUMERO***"""

def square_digits(num):
    num = str(num)
    ans = ''
    for i in num:
        ans += str(int(int(i)**2)) 
        
    return int(ans)

print(square_digits(int(input('Dime un número: '))))

"""# ***SUMAR DIGITOS***"""

def sum_digits(number):
    return sum([int(x) for x in str(number)])
print(sum_digits(int(input('Dime un número: '))))

"""# ***PALABRA ALREVEZ***"""

def spin_words(sentence):
    return sentence[::-1]

print(spin_words(input('Dime una palabra: ')))

"""# ***TRIBONACCI***
Hacer una secuercia donde sume los anteriores 3 numeros hasta llegar al n-abo elemento de la lista. **rango = n**


"""

def tribonacci(trio_inicial, rango):
    #len(Lista final)
    hasta = rango

    #lista = [0,1,2]
    lista = trio_inicial
    contador =0
    while contador < rango - 3:
        
        operacion = lista[contador] + lista[contador+1] + lista[contador+2]
        lista.append(operacion)
        contador +=1
           
    return lista

trio_inicial = [2,5,21]
n = 19
print(tribonacci(trio_inicial, n))

"""# ***PERMUTAR***"""

def inserta(x, lst, i):
    return lst[:i] + [x] + lst[i:]

def inserta_multiple(x, lst):
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]    

def permuta(c):
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s)
                for s in permuta(c[1:])],
                [])

lista = [1,2,3]
print(permuta(lista))

