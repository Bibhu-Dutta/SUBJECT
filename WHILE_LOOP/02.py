# Even numbers between 1 to 50.

# Approach 01:

print('Even Numbers Between 1 to 50.')
init = 1
while init < 51:
  if init % 2 == 0:
    print(init)
  init += 1

# Approach 2:

init = 2
while init < 51:
  print(init)
  init += 2