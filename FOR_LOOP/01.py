# Check if a sub-string is part of a given string

# Approach 01:
string = input('Enter A String: ')
sub = input('Enter A Sub-String: ')
sub_l = len(sub)
count = 0
for ip in range(len(string)):
  if(string[ip:sub_l+ip] == sub):
    count += 1
print(count)

# Approach 02: To avoid un-necessary comparison:
string = input('Enter A String: ')
sub = input('Enter A Sub-string: ')
count = 0
for ip in range(len(string) - len(sub)+1):
  if(string[ip: ip+len(sub)] == sub):
    count += 1
print(count)