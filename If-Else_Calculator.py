num1 = float(input('Enter Number: '))
operator = input('Enter Operator: ')
num2 = float(input('Enter Number: '))

if operator == '+':
    print('=', num1 + num2)
elif operator == '-':
    print('=', num1 - num2)
elif operator == '/':
    print('=', num1 / num2)
elif operator == '*':
    print('=', num1 * num2)
else:
    print('Invalid Operator')
