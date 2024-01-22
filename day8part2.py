input = open("inputday8.txt")
data = input.read()

data = data.splitlines()

#print(data)

instruction = []
instruction.extend(data[0])

code = []
code = data[2:]

mapped_code = []
for c in code:
    start = c[:3]
    left = c[7:10]
    right = c[12:len(c)-1]
    mapped_code.append([start, left, right])

start_items = []

for mC in mapped_code:
    mc_char = []
    mc_char.extend(mC[0])

    if mc_char[2] == "A":
        start_items.append(mC[0])


print(start_items)

steps_required = []

for sI in start_items:
    item = sI
    steps = 0

    look = True

    while look:
        for i in instruction:
            n = 0
            for c in mapped_code:
                if item == c[0]:
                    row = n
                    break
                else:
                    n = n+1
    
            if i == "L":
                item = mapped_code[row][1]
         
                steps = steps+1
     
            else:
                #right
                item = mapped_code[row][2]
                steps = steps+1
            
            if item[2] == "Z":
                steps_required.append(steps)
                look = False
                break
                
    
    steps_required.append(steps)

print(steps_required)

maxSteps = max(steps_required)

check = True
mult = 1
while check:
    for s in steps_required:
        if (maxSteps*mult)%s == 0:
            check = False
            continue
        else:
            mult = mult+1
            check = True
            break

print(maxSteps*mult)




#now find lowest common denominator


