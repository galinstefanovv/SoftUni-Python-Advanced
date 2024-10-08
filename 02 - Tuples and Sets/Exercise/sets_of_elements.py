start = [int(n) for n in input().split(' ')]
c , m = start
data = c + m
a = set()
b = set()
for _ in range(c):
    names = input()
    a.add(names)
for _ in range(m):
    names = input()
    b.add(names)
for unique in a.intersection(b):
    print(unique)
