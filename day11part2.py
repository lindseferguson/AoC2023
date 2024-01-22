input = open("inputday11.txt")
data = input.read()

data = data.splitlines()

#find empty rows and add extra row after
#find empty columns and add extra column

inserts_row = []
i = 0
for line in data:
    if "#" in line:
        i = i+1
        continue
    else:
        inserts_row.append(i)
        i = i+1

map_data = []
for line in data:
    line_char = []
    line_char.extend(line)
    map_data.append(line_char)

i = 0

inserts_col = []
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
        inserts_col.append(i)
        
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

i = 0
for row in inserts_row:
    if i > 0:
        row = row+i*(1000000-1)
    for mV in map_values:
        if mV[1] > row:
            mV[1] = mV[1]+(1000000-1)
    i = i+1

i = 0

for col in inserts_col:
    if i > 0:
        col = col+i*(1000000-1)
    for mV in map_values:
        if mV[2] > col:
            mV[2] = mV[2]+(1000000-1)
    i = i+1

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
  
    

