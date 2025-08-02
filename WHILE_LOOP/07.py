# Sum of index positions of all consonants present in a given string:

print('CONSONANT INDEX POSITION SUM')
string = input('Enter A String: ')
index = 0
index_sum = 0
while index < len(string):
  if(string[index].isalpha() and string[index] not in 'aeiouAEIOU'):
    index_sum += index
  index += 1
print('Sum Of Index Positions Of Consonants: ', index_sum)