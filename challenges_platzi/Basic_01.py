def back(name):   
    print(f'Do you want to return to another activity?')
    desicion_x = input('''(1) Yes    (2) No, bye\n''')

    if desicion_x == "1":
        print(actividad(name))
    else: print('ok! bye')

def add(a,b):
    result = a + b
    print(f'{a} + {b} = {result}')
    return result

def restar(a,b):
    result = a + b
    print(f'{a} - {b} = {result}')
    return result

def divide(a,b):
    if a > b and b != 0:
        print(f'In the number {b} it is {a/b} times in {a}')
    elif b > a and a != 0:
        print(f'In the number {a} it is {b/a} times in {b}')
    elif a == b:
        print(f'{a} and {b} are the same number, so they are once upon a time on themselves.')
    elif a > b and b == 0 or b > a and a == 0:
        print(f'As the minor is 0, in Mathematics it would be indeterminate or Infinite.')
    

def cal_div(total, num_people, percentage):
    tip = (total * percentage)/100
    every_people = (total + tip)/num_people
    print(f'\n ach person pays ${every_people}')

def pasar(days):
    hours = days * 24
    minutes = hours * 60
    seconds = seconds * 60
    print(f'''
    {days} days
    {hours} hours
    {minutes} minutes
    {seconds} seconds
    ''')

def kilometers(milles):
    if milles == 1:
        print('One mile = 1.609344 Km')
    else:
        km = milles * 1.609344
        print(f'That {milles} milles is {km} kilometers')
    


def actividad(name):
    print(f'{name}, What do you want to do?')

    activity = input('''
    (1) Add a pair of numbers
    (2) Subtract pizzas
    (3) Add 2 and Multiply by another one
    (4) Past and Future Age
    (5) Dividing the account
    (6) Calculating days
    (7) Converting Miles
    (8) Dividing
    ''')

    if activity == '1':
        num_1 = float(input('1° number: '))
        num_2 = float(input('2° number: '))
        add(num_1,num_2)
        back(name)

    elif activity == '2':
        print('''You came to a party, You bring the pizza''')
        pieces = float(input('How many slices of pizza are you carrying? : '))
        pass_2 = input('''After a while I see:
        (1) What was left over...      (2) What they ate...
        ''')

        if pass_2 == "1":
            Left_over = float(input('Left over: '))
            food = pieces - Left_over
            print(f'They ate {food} portions. WOW!')
        elif pass_2 == "2":
            food = float(input('What they ate: '))
            Left_over = pieces - food
            print(f'There are still {Left_over} portions left' )
        else:
            print(f'So here we refer to the famous phrase: \n "I just know, that I don it know." ')

        back(name)

    elif activity == '3':
        print('Add')
        num_1 = float(input('1° number: '))
        num_2 = float(input('2° number: '))
        print('Multiply for : ')
        num_3 = float(input('3° number: '))
        result = add(num_1,num_2) * num_3
        print(f'({num_1} + {num_2}) * {num_3} = {result}')
        volver(name)

    elif activity == '4':
        age_current = int(input('What is your current age? : '))
        back = int(input('How many years do you want us to come back? : '))   
        go_to = int(input('How many years do you want us to add? : '))

        print(f' {name} you are currently {age_current}. \n {back} years ago you were {age_current - back} years old.\n In {go_to}  years you will be {age_current + go_to}')
        back(name)

    elif activity == '5':
        print('You go with your friends to your favorite restaurant and agree to split the bill.')
        total = float(input('How much did they have to pay? : '))
        people = int(input('How many people do we split the bill between? : '))
        tip = float(input('How much of a percentage will be left as a tip? : '))
        cal_div(total, people, tip)
        back(name)

    elif activity == '6':
        days = int(input('How many days? \n'))
        pasar(days) 
        back(name)

    elif activity == '7':
        print('Milles to Kilometers') 
        milles = float(input('Milles: '))
        kilometers(milles)
        back(name)

    elif activity == '8':
        print('Tell me two numbers')
        num_1 = float(input('1° number: '))
        num_2 = float(input('2° number: '))
        divide(num_1,num_2)
        back(name)


if __name__ == "__main__":
    print('''Hi, Ready for the challenges?''')
    name = input('What is you name? \n')
    print(f'Ok! {name} and do you have a last name? \n')
    pass_1 = input('''(1) Yes     (2) No\n''')

    if pass_1 == "1":
        last_name = input('What is your last name?\n')
        print(f'{name} {last_name}, At your command.')
    else:
        print(f'O ok! only {name}\n')
    
    activity(name)