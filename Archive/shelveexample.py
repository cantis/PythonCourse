import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange citris fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citris fruit"
    fruit['grape'] = "a small, sweet fruit frowing in bunches"
    fruit['lime'] = "a sour, green citris fruit"

    print(fruit["lemon"])
    print(fruit["grape"])
