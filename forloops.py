number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char
    
newNumber = int(cleanedNumber)
print("The number is {}",format(newNumber))

for state in ["not pinin'", "no more", "a stiff", "befeft of lift"]:
    print("This parrot is "+ state)

