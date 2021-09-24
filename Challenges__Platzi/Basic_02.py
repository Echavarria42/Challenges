def more_minor(a,b):
    if a > b: print(f'{a} is greater than {b}')
    elif a < b: print(f'{b} is greater than {a}')
    elif a == b: print('Are the same number')

def stable_range(lim,num):
    if num < lim : print(f'The number {num} is found in the range.')
    elif lim < num: print(f'The number {num} exceeds the allowed limit.')
    elif  lim == num : print('You are on the edge, be careful.')

def changeable_range(lim_1,lim_2,comparison):
    if lim_1 < lim_2:
        lim_lower = lim_1
        lim_upper = lim_2
    elif lim_2 < lim_1:
        lim_lower = lim_2
        lim_upper = lim_1
    elif lim_1 == lim_2 and comparison == lim_1: return print('En serio? los 3 iguales?')
    elif lim_1 == lim_2 and comparison < lim_1: return print(f'{comparison} is less than {lim_1}')
    elif lim_1 == lim_2 and comparison > lim_1: return print(f'{comparison} is greater than {lim_1}')

    if comparison < lim_upper and comparison > lim_lower:
        print(f'{comparison}is within the range of{lim_lower} and {lim_upper}')
    elif comparison > lim_upper: print(f'{comparison} exceeds {lim_upper} por {comparacion - lim_superior}')
    elif comparison < lim_lower: print(f'{comparison} is below the limit')
    elif comparison == lim_lower and comparison != lim_upper : print('Careful, you are at the lower limit!')
    elif comparison == lim_upper and comparison != lim_lower : print('Wow! you are about to go out of bounds')
    else: print('Try to get the numbers right next time.')

def i_like_turtles(animal):
    animal = animal.lower()
    animal = animal.replace(" ", "")
    if animal== 'tortuga' or animal == 'turtles': print('I also like turtles')
    else: print('That animal is cool, but I prefer the turtles.')

def weather():
    print('Just answer yes or no to the questions')
    pass_1 = input('\nQuestion, Is it raining? \n')
    if pass_1.lower() == 'yes':
        pass_1_2 = input('\nAnd tell me, is it windy? \n')
        if pass_1_2.lower() == 'yes' :
            print('\nIf it is very windy, it will be difficult to go out with a small spare')
        elif pass_1_2.lower() == 'no':
            print('\nIf you are going out, take an umbrella with you.')
        
    elif pass_1.lower() == 'no':
        pass_2_2 = input('\nSo it is a cool day? \n') 
        if pass_2_2.lower() == 'yes' :
            print('\nWhat a pleasant climate')
        elif pass_2_2.lower() == 'no':
            print('\nThe best thing to do is to look for a swimming pool')
    else:
        print('\n So "I just know that I do not know anything".')

    print('Have a nice day')

def allowed_age(age):
    if age > 30: print('It is never too late to learn. What course will we take?')
    elif age >= 18 and edad < 30: print('This is an excellent time to boost your career.')
    elif age < 18: print('Do you know where to direct your future? I can surely help you.')
    
def numbered_messages(number):
    if number == '1':
        print('Today we will learn about prorgamation')
    elif number == '2':
        print('How about taking a digital marketing course?')
    elif number == '3':
        print('Today is a great day to start learning about design.')
    elif number == '4':
        print('What if we learn something about online business?')
    elif number == '5':
        print('Let is take a look at a couple of classes on audiovisual production.')
    elif number == '6':
        print('It may be good to develop a soft skill at Platzi')
    else:
        print('I do not have a message for that')

def main():
    pass

if __name__ == '__main__':
    main()