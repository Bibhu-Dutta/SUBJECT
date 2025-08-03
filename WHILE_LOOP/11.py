# Print how many times a given sub-string is present in a string

string = input('Enter A String: ')
sub_s = input('Enter Sub-string To Search: ')
index = 0
count = 0
while index < len(string):
  if(string[index].lower() == sub_s):
    count += 1
  index += 1
print(f'{sub_s} is in {string} for {count} times!')