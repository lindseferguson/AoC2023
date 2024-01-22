input = open("inputday15.txt")
data = input.read()

data = data.split(",")


total = 0

boxes = [[None]]*256

for item in data:
    cV = 0
    val = ""
    char = []
    char.extend(item)
    
    add = False
    for c in char:
        if c == "=":
            add = True
        elif c == "-":
            b = int(cV)
            temp = boxes[b]

            if temp == [None] or len(temp) == 0:
                #nothing in the box
                break
            else:
                for i in temp:
                    if i[0] == val:
                        boxes[b].remove(i)
        else:
            if add:
                #adding the lens
                b = int(cV)
                temp = boxes[b]

                if temp == [None] or len(temp)==0:
                #nothing in the box
                    boxes[b]=[[val,c]]
                else:
                    insert = False
                    count = 0
                    for i in temp:
                        if i[0] == val:
                            boxes[b][count]=[val,c]
                            insert = True
                        count = count+1
                    if insert == False:
                        boxes[b].append([val,c])
            
            else:

                ascii_value = ord(c)
                cV = ascii_value+cV
                cV = cV*17
                cV = cV%256
                val = val+c

count = 0
total = 0
for box in boxes:
    if box == [None]:
        count = count+1
        continue
    else:
        pos = 1
        for item in box:
            power = (count+1)*pos*int(item[1])
            print(power)
            total = total+power
            pos = pos+1
    count = count+1

print(total)



