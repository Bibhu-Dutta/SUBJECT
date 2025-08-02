# Sum of even digits present at even index positions in a given string:

string = input('Enter A String: ')
index = 2
even_sum = 0
while index < len(string):
  if(string[index].isdigit() and int(string[index]) % 2 == 0):
    even_sum += int(string[index])
  index += 2
print('Sum Of Even Digits Present At Even Index Postions In String: ', even_sum)