# Sub lista Creciente 
def subCreciente(arr):
  sumalistas = []
  aux = arr[::]
  for i in range(len(arr)):
    count = 0
    lista_num = [arr[i]]
    aux.remove(arr[i])
    for j in range(len(aux)):
      if lista_num[count] < aux[j]:
        lista_num.append(aux[j])
        count += 1
    sumalistas.append(len(lista_num))
  
  return max(sumalistas)

#   lista = [10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90]
#  lista_1 = [9, 9, 4, 2]


# DIVISION DE PALABRA ENTRE FRAGMENTOS DADOS
def DividorPalabra(strArr):
  for i in range(len(strArr[0])):
    if strArr[0][:i+1] in strArr[1] and strArr[0][i+1:] in strArr[1] and strArr[0][:i+1] + strArr[0][i+1:] == strArr[0]:
      return f'{strArr[0][:i+1]},{strArr[0][i+1:]}'
  return "not possible"

#  lista_1 = ["abcgefd", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]
#  lista = ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
  

# Columnas Suma Mayor tamaño igual altura
def ArrayChallenge(arr):
  lista = []

  for i in range(len(arr)):
    h = arr[i]
    newarr = arr[::]
    newarr.remove(arr[i])
    for j in range(len(arr)-1):
      if newarr[j] >= arr[i]:
        h += arr[i]
      else:
        lista.append(h)
  return max(lista)

# lista = [6, 3, 1, 4, 12, 4]
# lista_1 = [5, 6, 7, 4, 1]
# lista_2 = [2, 1, 3, 4, 1]

# Promedio igual a moda
def Prom_Moda(arr):
  count = {}
  for i in arr:
    count[arr.count(i)] = i
  promedio = int(sum(arr)/len(arr))

  if promedio == count[max(count)]:
    return 1
  else:
    return 0

#   lista = [5, 3, 3, 3, 1] 

# 2X2 de VOCALES EN UNA MATRIZ
vocales = ["a", "e","i", "o", "u"]
def vocales2X2(strArr):
  for i in range(int(len(strArr)-1)):
    for j in range(int(len(strArr[0])-1)):
      if strArr[i][j] in vocales and strArr[i][j+1] in vocales and strArr[i+1][j] in vocales and strArr[i+1][j+1] in vocales:
       return(f"{i}-{j}")
       break
      
  return "not found"

#  matriz = ["abcd", "eikr", "oufj"]
#  matriz_1 = ["aqrst", "ukaei", "ffooo"]
# matriz_2 = ["gg", "ff"]


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

