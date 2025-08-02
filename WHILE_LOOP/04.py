# Sum of index positions of vowels present in a string:

string = input('Enter A String: ')
index = 0
index_sum = 0
while index < len(string):
  if(string[index] in 'aeiousAEIOU'):
    index_sum += index
  index += 1
print('Sum Of Index Postions: ', index_sum)