# Sum of first n numbers:

n = int(input('Enter A Number: '))
init = 1
n_sum = 0
while init <= n:
  n_sum += init
  init += 1
print(f'Sum Of Numbers Till {n}: {n_sum}')