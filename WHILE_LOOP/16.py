# Sum of digits present in a given string

string = input('Enter A String: ')
sum = 0
index = 0
while index < len(string):
  if(string[index].isdigit()):
    sum += int(string[index])
  index += 1
print(sum)