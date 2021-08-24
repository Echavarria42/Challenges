
def euclides(num_1,num_2,iteracciones=1):
    if num_1<num_2:
        num_1,num_2=num_2,num_1

    resto=num_1%num_2
    print(f'{num_1} = {num_2} * {int((num_1 - resto)/num_2)} + {resto}')
    if resto==0:
        return (num_2,iteracciones)

    return euclides(num_2,resto,iteracciones+1)

num_1=int(input('Numero 1° = '))
num_2=int(input('Numero 2° = '))

comunDivisor,iteracciones=euclides(num_1,num_2)

print(f'''
MCD ( {num_1} , {num_2} ) = {comunDivisor}''')
