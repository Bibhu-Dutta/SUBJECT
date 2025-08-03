# How many integers are present in a given list

# using isinstance() function:
list = eval(input('Enter A List: '))
index = 0
count = 0
while index < len(list):
  if(isinstance(list[index], int)):
    count += 1
  index += 1
print(count)

#using type() function:
list = eval(input('Enter A List: '))
count = 0
index = 0
while index < len(list):
  if(type(list[index]) == int):
    count += 1
  index += 1
print(count)