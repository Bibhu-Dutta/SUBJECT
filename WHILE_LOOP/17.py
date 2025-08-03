# Absolute difference of all even integers and odd integers present in a given list

list = eval(input('Enter A List: '))
even_sum = 0
odd_sum = 0
index = 0
while index < len(list):
  if(isinstance(list[index], int)):
    if(list[index] % 2 == 0):
      even_sum += list[index]
    else:
      odd_sum += list[index]
  index += 1
print(f'Even Sum: {even_sum}, Odd Sum: {odd_sum}')
if(even_sum > odd_sum):
  diff = even_sum - odd_sum
else:
  diff = odd_sum - even_sum
print('Absolute Difference: ', diff)

# Using abs()
list = eval(input('Enter A List: '))
even_sum = 0
odd_sum = 0
index = 0
while index < len(list):
  if(isinstance(list[index], int)):
    if(list[index] % 2 == 0):
      even_sum += list[index]
    else:
      odd_sum += list[index]
  index += 1
print(f'Even Sum: {even_sum}, Odd Sum: {odd_sum}')
print('Absolute Difference: ', abs(even_sum, odd_sum))