def operate(operator, *args):
    if operator == '+':
        return sum(args)
    elif operator == '-':
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
        return result
    elif operator == '/':
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
    else:
        return "Invalid operator"