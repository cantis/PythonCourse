address = input("Ip Address: ")
segmentCount = 1
segmentLength = 0
i = ""

for i in address:
    #print(i)    
    if i == '.':
        print("Segment {} length {}".format(segmentCount, segmentLength))
        segmentCount += 1
        segmentLength = 0
        continue
    segmentLength += 1
if i != '.':        
    print("Segment {} length {}".format(segmentCount, segmentLength))