# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)

# for animal in farm_animals:
#     print(animal)

# print("=" * 40)

# wild_animals = set(["lyon", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)

# for animal in wild_animals:
#     print(animal)

# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)
# even = set(range(0, 40 ,2))
# print(even)
# print(len(even))

# squares_tuple = (4,6,9,16,25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))

# print(even.union(squares))
# print(len(even.union(squares)))

# print("-" * 40)

# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

# even = set(range(0, 40 ,2))
# print(sorted(even))
# squares_tuple = (4,6,9,16,25)
# squares = set(squares_tuple)
# print(sorted(squares))

# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))

# print("squares minus even")
# print(squares.difference(even))
# print(squares - even)

# print("=" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))

even = set(range(0, 40 ,2))
print(sorted(even))
squares_tuple = (4,6,9,16,25)
squares = set(squares_tuple)
print(sorted(squares))

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))
print("symetric squares minus even")
print(squares.symmetric_difference(even))