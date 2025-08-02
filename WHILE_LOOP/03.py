# Factorial Of A Number:

num = int(input('Enter A Number: '))
fact = 1
init = 1
while init <= num:
  fact *= init
  init += 1
print(fact)