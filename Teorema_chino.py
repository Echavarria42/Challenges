def multiplicar(lst):
    solution = 1
    for i in lst:
        solution *= i
    return solution

def Encontrar_inverso(Cd_n,mod):
    rango = list(range(mod))
    rango.reverse()
    for i in rango:
        a = ((Cd_n*i)-1)/ mod
        b = ((Cd_n*i)-1)// mod
        if a == b :
            return i


def chino(residuo, modulo,n):
    producto = multiplicar(modulo)
    Cd_n = [int(producto/i) for i in modulo]
    Dd_n = [ Encontrar_inverso(Cd_n[i], modulo[i]) for i in range(n)]
    pre_final = [ residuos[i] * Cd_n[i] * Dd_n[i] for i in range(n)]
    final = sum(pre_final)
    return print(f'{final%producto} + {producto}t')
   # Final = producto 




if __name__ == '__main__':
    n = int(input('dime cuantas ecuaciones son: '))
    residuos = []
    modulos = []
    for i in range(n):
        print(f' x = a_{i+1} mod b_{i+1}')
        residuo_x = int(input(f'a_{i+1} = dime el residuo: '))
        modulo_x = int(input(f'b_{i+1}° = dime el modulo: '))
        print(f'\n x = {residuo_x} mod {modulo_x} \n')
        residuos.append(residuo_x)
        modulos.append(modulo_x)
    
    chino(residuos, modulos, n)