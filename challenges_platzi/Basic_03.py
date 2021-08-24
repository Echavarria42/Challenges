def length(word):
    word = word.replace(' ','')
    return print(f'\n Your string has {len(word)} letters')

def sum_initials(name, last_name, food, Country):
    return print(f'''    
    Name: {name.title()}
    Last_Name: {last_name.title()}
    Country: {Country.title()}
    You name is {name.title()} {last_name.title()} and your favory food is {food}''')

def fragment(sentence, r_initial, r_end):
    return print(word[r_initial-1:r_end])
    
def Upp_Low(pal_1, pal_2):
    return print(f'{pal_1.upper()} {pal_2.lower()}')

def if_nombre(nombre, apellido):
    if len(nombre) > 5:
        return print(f'Hello {nombre.title()} \n')
    else: 
       return print(f'Hello {nombre.title()} {apellido.title()} \n')
    
def pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word.lower()[0] in vowels:
        word += 'way'
        print(word)
    else:
        word = word[1:] + word[0] + 'ay'
        print(word.title())

if __name__ == "__main__":
    word = input('Tell me a word: ')
    length(word)

    print('\n Everything you answer should be in lowercase letters.')
    name = input('\n What is your name? \n')
    last_name = input('\n What is your Last name? \n')
    food = input('\n What is your favorite food? \n')
    Country = input('\n Where are you from? \n')
    sum_initials(name, last_name, food, Country)

    print('\n Let us fragment a sentence')
    word = input('\n Tell me a sentence of more than 10 letters \n')
    r_initial = int(input('\n Tell me the number where to start: '))
    r_end = int(input('\n Tell me the number where to end: '))
    fragment(word, r_initial, r_end)

    print('\n Tell me 2 words \n ')
    pal_1 = input('first word: ')
    pal_2 = input('second word: ')
    Upp_Low(pal_1, pal_2)

    if_nombre(name, last_name)

    palabra_pig = input('\n Give me a word and I all pass it on to Pig Latin. \n')
    pig_latin(palabra_pig)
    