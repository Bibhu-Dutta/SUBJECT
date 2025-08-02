# Replace vowels with thier index positions:

string = input('Enter A String: ')
index = 0
new_string = ''
while index < len(string):
  if(string[index] in 'aeiouAEIOU'):
    new_string += str(index)
  else:
    new_string += string[index]
  index += 1
print("New String: ", new_string)