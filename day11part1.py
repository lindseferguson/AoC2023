input = open("inputday11.txt")
data = input.read()

data = data.splitlines()

#find empty rows and add extra row after
#find empty columns and add extra column

print(data)
inserts = []
i = 0
for line in data:
    if "#" in line:
        i = i+1
        continue
    else:
        inserts.append([i,len(line)])
        i = i+1

i = 0

for IN in inserts:
    row = "."*IN[1]
    data.insert(IN[0]+i,row)
    i = i+1

map_data = []
for line in data:
    line_char = []
    line_char.extend(line)
    map_data.append(line_char)

i = 0

inserts = []
while i < len(map_data[0]):
    add = True
    j = 0
    while j < len(map_data):
        if map_data[j][i] == "#":
            add = False
            break
        else:
            j = j+1
    
    if add:
        inserts.append(i)
        
    i = i+1

i = 0
for col in inserts:
    for row in map_data:
        row.insert(col+i,".")
    i = i+1

i = 1
map_values = []

r = 0
for row in map_data:
    j = 0
    while j < len(row):
        if row[j] == "#":
            row[j] = i
            map_values.append([i,r,j])
            i = i+1
        j = j+1
    r = r+1

print(map_values)

i = 1
answer = 0
j = 1
for mV in map_values:
    i = j
    while i < len(map_values):
        
        a = abs(map_values[i][1]-mV[1])
        b = abs(map_values[i][2]-mV[2])
        dist = a+b
        answer = answer+dist
        i =i+1
        
    j = j+1

print(answer)
    
    

