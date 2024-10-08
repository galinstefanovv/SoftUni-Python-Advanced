n = int(input())
chemical = [input().split() for _ in range(n)]
uniques = set()
for first in chemical:
    for second in first:
        uniques.add(second)
for element in uniques:
    print(element)