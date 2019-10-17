
with open("sample.txt","a") as twoTimes:
    for r in range(1,13):
        print("{0:2} times 2 is {1}".format(r, r*2), file=twoTimes)

