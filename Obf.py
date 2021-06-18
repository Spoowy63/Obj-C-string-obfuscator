import string
import random
import os

# Made by: github.com/Spoowy63

string_to_obf = input('Paste the text you want encrypted: ')
filler_length = input('Filler length (leave empty for default value): ')

variable_name = "A" + str(random.randint(1000, 9999))

if filler_length == "":
	filler_length = 18
else:
	filler_length = int(filler_length)


letters_list = []

for characters in string_to_obf:
	letters_list.append(characters)


combined_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits

filler = "".join(random.choices(combined_characters, k=filler_length))

finished_obf_string = filler.join(letters_list)


os.system('clear||cls')
print('\nCopy the code below for your project:\n')
print("//Made by: github.com/Spoowy63")
print(f"NSString *{variable_name}; \n{variable_name} = [@\"{finished_obf_string}\" stringByReplacingOccurrencesOfString:@\"{filler}\" withString:@\"\"];")
