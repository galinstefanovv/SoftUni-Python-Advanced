def repeat_text(text, number):
    return text * number

try:
    text = input()
    number = int(input())
    print(repeat_text(text, number))
except ValueError:
    print("Variable times must be an integer")