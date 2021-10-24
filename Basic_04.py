import math

def multiply(a,b):
    print(a*b)
    return (a*b)

def round(num, dig):
    if dig == 0:
        return print(int(num))
    else:
        a = round(num, dig)
        return print(a)

def root(a):
    return print(round((a**0.5),3))

def circle(radius):
    return (math.pi*(radius**2))

def cylinder(radius, height):
    return (circle(radius) * height)

def residual_whole(num, divider):
    whole = int(num // divider)
    waste = num - (whole*divider) 
    if whole == 1 and waste == 0:
        print(f'Son los mismos numeros')
    elif waste == 0:
        print(f'The number {divider} is {whole} times, without residue')
    else:
        print(f'The number {divider} is {whole} times, and {waste} is left over.')

def area_perimeter(num_sides,  side_distance):
    perimeter = num_sides* side_distance
    a = 360/num_sides
    apothem = ( side_distance/2)/math.tan(math.radians(a/2))
    area = (perimeter * apothem)/2
    print(f'perimeter = {perimeter} \nArea = {area}')

if __name__ == "__main__":
    print('Tell me two number for multiply')
    num_1 = float(input('1° number: '))
    num_2 = float(input('2° number: '))
    num_mult = multiply(num_1, num_2)

    dig = int(input('\nHow many figures do I approximate? : '))
    round(num_mult, dig) 

    num_3 = float(input('\nGive me a number, I square root it: '))
    root(num_3) 

    radius = float(input('\nTell me the radius of a circle: '))
    print(f'The area of the circle is: {circle(radius)}')

    print('\nVolume of a cylinder')
    radius_cylinder = float(input('Tell me the radius of the base : '))
    cylinder_height = float(input('Tell me the height of the cylinder : '))
    print(f'The volume of the cylinder is: {cylinder(radius_cylinder, cylinder_height)}') 

    whole = float(input('Tell me a number : '))
    divider = float(input('Tell me the divider : '))
    residual_whole(whole, divider)

    print('\nI tell you the area and perimeter of any regular polygon.')
    number_sides = float(input('Tell me how many sides it has : '))
    sides = float(input('How long each side is : '))
    area_perimeter(number_sides,sides  )