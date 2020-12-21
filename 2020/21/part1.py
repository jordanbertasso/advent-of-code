import fileinput

lines = [l.strip() for l in fileinput.input()]

# Map from allergen to all foods that contain the allergen
A = {}

# Map of all ingredients and their times seen
I = {}

for food in lines:
    ingredients = food.split('(')[0]
    ingredients = ingredients.split()

    for ing in ingredients:
        I.setdefault(ing, 0)
        I[ing] += 1

    allergens = food.split('(')[1][:-1].split()[1:]
    allergens = list(map(lambda x: x.replace(',', ''), allergens))

    for allergen in allergens:
        A.setdefault(allergen, [])
        A[allergen].append(ingredients)

maybe_impossible = {}
for ingredient in I:
    for allergen in A:
        if not all(ingredient in food for food in A[allergen]):
            maybe_impossible.setdefault(allergen, [])
            maybe_impossible[allergen].append(ingredient)

impossible = []
for ingredient in I:
    good = True

    for allergen in maybe_impossible:
        if ingredient not in maybe_impossible[allergen]:
            good = False
            break

    if good:
        impossible.append(ingredient)

ans = 0
for ing in impossible:
    ans += I[ing]

print(ans)
