def favory_course(n, course):
    for i in range(8): print(course)
    for i in range(n): print(course)

def acrostic(word):
    for i in list(word): print(i)

def favory_animal(n, word):
    for i in range(n):
        acrostic(word)

def table_mult(n):
    for i in range(10):
        print(f'{n} * {i+1} = {(i+1)*n}')

def count_down(n):
    if n>0:
        for i in range(n+1): print(f'{n-i}')
    elif n<0:
        for i in range(n+1): print(f'{n+i}')
    else: print(0)

def over_fiveteen(n, course):
    if n > 15 :
        prin('the number is very large')
        for i in range(3): print(course)
    else: 
        for i in range(n): print(course)

def sum_four(n, x):
    if n == 1:
        print(sum(x))
    elif n== 2:
        print('I do not add it')
    else:
        print('What to ask?')

def line(s, m):
    if s == 1:
        for i in range(m+1): print(i)
    elif s == 2:
        for i in range(m+1): print(f'{m-i}')


def main():
    name_course = input('what is your favory course? : ')
    number_course = int(input('How many times do I repeat it? : '))
    favory_course(number_course, name_course)


    word = input('Tell me a word: ')
    acrostic(word)


    animal = input('Tell me an animal: ')
    number_animal = int(input('How many times do I repeat it? : '))
    favory_animal(number_animal, animal)


    number_table = int(input('Tell me a number: '))
    table_mult(number_table)


    number_cDown = int(input(('Tell me a number: ')))
    count_down(number_cDown)


    number_course = int(input('How many times do I repeat it? : '))
    over_fiveteen(number_course, name_course)

    four_numbers = []
    for i in range(4): 
        number = int(input('Tell me a number: '))
        four_numbers.append(number)
    yes_not = int(input('''(1) Adding numbers
    (2) Do not add them
    
    '''))
    sum_four(yes_not, four_numbers)

    sign = int(input('''(1) Positive line
    (2) Negative line
    
    '''))
    lim = abs(int(input('Tell me a number: ')))
    line(sign, lim)

if __name__ == '__main__':
    main()