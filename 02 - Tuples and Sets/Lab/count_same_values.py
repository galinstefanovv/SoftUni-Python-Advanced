values = tuple(map(float, input().split(' ')))
counter_of_values = {value: values.count(value) for value in values}

for k, v in counter_of_values.items():
    print(f'{k} - {v} times')