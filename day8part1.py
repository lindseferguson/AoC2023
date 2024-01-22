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


#row = mapped_code.index(item)
#print(row)

item = "AAA"
steps = 0

while item != "ZZZ":
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
        
        if item == "ZZZ":
            break
     

print(steps)
    


