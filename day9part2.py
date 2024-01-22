input = open("inputday9.txt")
data = input.read()

data = data.splitlines()

history = []
split_item = []

answer = 0

for item in data:
    all_values = []
    split_item = item.split(" ")
    last_value = split_item[0]
    match = False
    items = split_item
    while match == False:
        i = 0
        values = []
        while i < len(items)-1:
            value = int(items[i+1])-int(items[i])
            values.append(value)
            i = i+1
        
        start = values[0]

        match = True
    
        for num in values:
            
            if start != num:
                match = False
                items = values

        
        all_values.append(values)


    all_values.reverse()

    hist = 0
    for line in all_values:
        if hist == 0:
            hist = hist+line[0]
        else:
            hist = line[0]-hist
        
    
    hist = int(last_value)-hist
    answer = answer+hist

print(answer)
