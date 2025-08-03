# Reverse A String:

# Approach 01:
string = input('Enter A String: ')
reverse = ''
index = 0
while index < len(string):
  reverse = string[index] + reverse
  index += 1
print(reverse)

# Approach 02: Using Positive Index
string = input('Enter A String: ')
reverse = ''
index = len(string)-1
while index >= 0:
  reverse += string[index]
  index -= 1
print(reverse)

# Approach 03: Using Negative Index
string = input('Enter A String: ')
reverse = ''
index = -1
while index >= -len(string):
  reverse += string[index]
  index -= 1
print(reverse)