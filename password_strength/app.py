password = input('Enter new password:')

result = {}
if len(password) >= 8:
    result['length'] = True
else:
    result['length'] =False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result['digits'] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True

result['upper'] = upper

if all(result.values()):
    print('Password is Strong')
else:
    print('Password is Weak')
