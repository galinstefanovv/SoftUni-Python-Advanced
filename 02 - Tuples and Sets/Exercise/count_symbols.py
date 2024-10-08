string = [element for element in input()]
my_dict = {}
for elements in string:
    if elements not in my_dict:
        my_dict[elements] = 0
    my_dict[elements] += 1

for k,v in sorted(my_dict.items()):
    print(f'{k}: {v} time/s')