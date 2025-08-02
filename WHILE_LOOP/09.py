# Index position of all vowels present in a given string

string = input('Enter A String: ')
index = 0
print('Index Position Of Vowel(s) In The String: ')
while index < len(string):
  if(string[index] in 'aeiouAEIOU'):
    print(index)
  index += 1