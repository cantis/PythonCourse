address = input("Ip Address: ")
if address[-1] != ".":
    address += "."
segmentCount = 1
segmentLength = 0

for i in address:
    if i == '.':
        print("Segment {} length {}".format(segmentCount, segmentLength))
        segmentCount += 1
        segmentLength = 0
        continue
    segmentLength += 1
