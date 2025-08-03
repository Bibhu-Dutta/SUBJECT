# Check if sub-string is part of a given string

string = input('Enter A String: ')
sub = input('Enter A Sub-string: ')
index = 0
count = 0
while index < len(string):
  if (string[index: index+len(sub)] == sub):
    count += 1
  index += 1
print(count)