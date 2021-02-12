import string
import random
import os


    # input text has to be atleast 2 letters long
a = input('Paste the text you want encrypted: ')
b = input('String length (leave empty for default value): ')

    # if you dont want symbols for example, change the 4th True to False

upper, lower, digit, symbol = True, True, True, False

    # this will consist of all the options you enabled

mix = ''

    # this will check if its true or not and if its true it will add it to mix variable

if upper:
    mix += string.ascii_uppercase
if lower:
    mix += string.ascii_lowercase
if digit:
    mix += string.digits
if symbol:
    mix += string.punctuation

    # this will be the variable for NSString
numb = str(random.randint(1000, 9999))
number = 'A' + numb

    # checking if input is empty or not, if empty use default value
if b == '':
    b = 18
else:
    b = int(b)

ec = ''.join(random.choices(mix, k=b))
ecs = ec.join(a)
os.system("clear")
print('\nCopy the code below for your project:\n')
print('//Made By Spoowy')
print(f"NSString *{number}; \n{number} = [\"{ecs}\" stringByReplacingOccurrencesOfString:@\"{ec}\" withString:@\"\"];")
