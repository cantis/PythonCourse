fruit = {"Orange": "a sweet, orange, citrus fruit",
"apple": "good for making cider",
"lemon": "a sour, yellow citris fruit",
"grape": "a small, sweet fruit growing in bunches",
"lime": "a sour, green citris fruit"}

while True: 
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key, "We don't have a " + dict_key)
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we don't have a " + dict_key)


