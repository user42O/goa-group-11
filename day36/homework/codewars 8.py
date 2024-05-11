def basic_math(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    elif operation == '-':
        return value1 - value2
    elif operation == '*':
        return value1 * value2
    elif operation == '/':
        return value1 / value2

print(basic_math('+', 4, 7))   
print(basic_math('-', 15, 18))  
print(basic_math('*', 5, 5))   
print(basic_math('/', 49, 7))  
