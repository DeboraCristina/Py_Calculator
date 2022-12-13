import re


def str_operators():
    return '\+|-|\*|x|%|/'


def str_digits():
    return '0|1|2|3|4|5|6|7|8|9'


def generate_expression(expression=None):
    if expression is None:
        return
    values = re.split(str_operators(), expression)
    operators = (re.split(str_digits(), expression))
    while '' in operators:
        operators.remove('')

    expression = []
    for i in range(len(values)):
        expression.append(values[i])
        if i < len(operators):
            expression.append(operators[i])
    return expression


def calculate_expression(expression=None):
    total = 0
    if expression is None:
        return
    # checking division and multiplication
    i = 0
    while '*' in expression or 'x' in expression or '/' in expression:
        if expression[i] == '/':
            total = int(int(expression[i - 1]) / int(expression[i + 1]))
            expression[i - 1] = str(int(int(expression[i - 1]) / int(expression[i + 1])))
            expression.pop(i + 1)
            expression.pop(i)
            i = i - 1
        if expression[i] == 'x' or expression[i] == '*':
            total = int(expression[i - 1]) * int(expression[i + 1])
            expression[i - 1] = str(int(expression[i - 1]) * int(expression[i + 1]))
            expression.pop(i + 1)
            expression.pop(i)
            i = i - 1
        i = i + 1
    # checking for %
    i = 0
    while '%' in expression:
        if expression[i] == '%':
            total = int(expression[i - 1]) % int(expression[i + 1])
            expression[i - 1] = str(int(expression[i - 1]) % int(expression[i + 1]))
            expression.pop(i + 1)
            expression.pop(i)
            i = i - 1
        i = i + 1
    # checking for sum and subtraction
    i = 0
    while '+' in expression or '-' in expression:
        if expression[i] == '+':
            total = int(expression[i - 1]) + int(expression[i + 1])
            expression[i - 1] = str(int(expression[i - 1]) + int(expression[i + 1]))
            expression.pop(i + 1)
            expression.pop(i)
            i = i - 1
        if expression[i] == '-':
            total = int(expression[i - 1]) - int(expression[i + 1])
            expression[i - 1] = str(int(expression[i - 1]) - int(expression[i + 1]))
            expression.pop(i + 1)
            expression.pop(i)
            i = i - 1
        i = i + 1

    return total


def check_math_expression(expression=None):
    if expression is None:
        return False
    for element in expression:
        if not element.isdigit() and element not in str_operators():
            return False
    return True


def calculator(expression=''):
    if not check_math_expression(expression):
        return 'False'
    for operator in str_operators():
        if operator in expression:
            break
    else:
        return expression

    expression = generate_expression(expression)

    return calculate_expression(expression)


if __name__ == '__main__':
    result = calculator(input("Your operation: "))
    print(result)
