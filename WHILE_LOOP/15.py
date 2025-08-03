# Special Characters, Digits and Alphabets present in a given string

string = input('Enter A String: ')
special = 0
alpha = 0
digit = 0
index = 0
while index < len(string):
  if(string[index].isalpha()):
    alpha += 1
  elif(string[index].isdigit()):
    digit += 1
  else:
    special += 1
  index += 1
print(f'Alphabet: {alpha}, Integer: {digit} and Special Character: {special}')