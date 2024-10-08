from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

created = []

items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit",
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    item = textile + medicament

    if items.get(item):
        created.append(items[item])
    elif item > 100:
        created.append(items[100])
        sums = abs(item - 100)
        medicaments[-1] += sums
    else:
        medicaments.append(medicament + 10)

if not textiles and medicaments:
    print(f"Textiles are empty.")
if not medicaments and textiles:
    print(f"Medicaments are empty.")
if not textiles and not medicaments:
    print(f"Textiles and medicaments are both empty.")

my_dict = {}
for item_created in set(created):
    my_dict[item_created] = created.count(item_created)

sorted_dict = sorted(my_dict, key=lambda x: (-my_dict[x], x))
[print(f"{item_created} - {created.count(item_created)}") for item_created in sorted_dict]
if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(medicaments))}")

if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
