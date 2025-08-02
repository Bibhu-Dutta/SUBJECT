# Even numbers withing given range:

LR = int(input('Enter Lower Range: '))
UR = int(input('Enter Upper Range: '))
# init = LR
if(LR < UR):
  while LR <= UR:
    if(LR % 2 == 0):
      print(LR)
    LR += 1
else:
  print('Invalid Range!')