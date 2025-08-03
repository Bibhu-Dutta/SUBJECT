# Check how many special characters are present in a given string

string = input('Enter A String: ')
count = 0
index = 0
while index < len(string):
  if(not string[index].isalnum()):
    count += 1
  index += 1
print(count)