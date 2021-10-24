import random

def fivety(n):
    number = n
    while n < 50:
        print(f'{number}+{n}={number+n}')
        n = number + n

def fourty_two():
    n = int(input('Tell me a number: '))
    if n>42:
        return print(f'{n} > 42')
    fourty_two()

def two_numbers(x,y):
    sum_two = x+y
    print(f'{x} + {y} = {sum_two}')
    pass_1 = int(input('''(1) Add another number
   (2) We do not add another number
   
   '''))
    if pass_1 == 1:
       other_number = int(input('Tell me a number: '))
       two_numbers(other_number, sum_two)
    
    
def list_inved(list_friends):
    counter = len(list_friends)
    pass_1 = int(input('''(1) We add another friend
   (2) We do not add another number
   
   '''))
    if pass_1 == 1:
        new_friend = input('New friend: ')
        list_friends.append(new_friend)
        list_inved(list_friends)
    print(f'{counter}')

def one_hundred():
    one = random.randint(1,100)
    print(one)
    number = 0
    counter = 0
    while number != one:
        counter += 1
        number = int(input('Tell me a number: '))
    print(f'{counter} attemps')

def main():
    number_fivety = int(input('Tell me a number: '))
    fivety(number_fivety)
    fourty_two()

    sum_one = int(input('Tell me a number: '))
    sum_two = int(input('Tell me a number: '))
    two_numbers(sum_one ,sum_two)

    friend = input('Tell me a name to friend: ')
    list_inved([friend])
    
    one_hundred()


if __name__ == '__main__':
    main()