import random
import string 
 
print("Made By FlipFlop")
a = input("paste text you want encrypted: ")
b = how_long_do_you_want_the_string_to_be = 18
 
 
#if you dont want symbols for example, change the 4th True to False
upper, lower, digit, symbol = True, True, True, True
 
#this will consist of all the options you enabled
mix = ""
 
 
#this will check if its true or not and if its true it will add it to mix variable 
if (upper):
    mix += string.ascii_uppercase
if (lower):
    mix += string.ascii_lowercase
if (digit):
    mix += string.digits
if (symbol):
    mix += string.punctuation
    
#this will be the variable for NSString
number = random.randint(1000,9999)
 
 
ec = "".join(random.choices(mix, k=b))
ecs = ec.join(a)
  
print(f"NSString *{number}; \n{number} = [\"{ecs}\" stringByReplacingOccurrencesOfString:@\"{ec}\" withString:@\"\"];")
