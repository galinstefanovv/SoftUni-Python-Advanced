def even_odd(*args):
    command = args[-1]
    result = []

    for n in args[:-1]:
        if int(n) % 2 == 0 and command == "even":
            result.append(n)
        elif int(n) % 2 == 1 and command == "odd":
            result.append(n)

    return result
