input = open("inputday13.txt")
dataTotal = input.read()

dataTotal = dataTotal.split("\n\n")

rowTotal = 0
colTotal = 0
for data in dataTotal:
    data = data.splitlines()

    rows = 0
    col = 0
    i = 0
    while i < len(data)-1:
        match = True
        j = 0
        while j < len(data[0]):
            if data[i][j] == data[i+1][j]:
                j = j+1
            else:
                match = False
                break
        if match:
            #found possible reflection line
            k = i-1
            l = i+2
            good = True
            while k >=0 and l < len(data):
                j = 0
                while j < len(data[0]):
                    if data[k][j] == data[l][j]:
                        j = j+1
                    else:
                        good = False
                        break
                if good == False:
                    break
                
                k = k-1
                l = l+1
            
            if good:
                #found reflection line (rows)
                rows = rows+i+1
                break
        
        i = i+1

    if rows == 0:
        #check columns for mirror

        i = 0
        while i < len(data[0])-1:
            match = True
            j = 0
            while j < len(data):
                if data[j][i] == data[j][i+1]:
                    j = j+1
                else:
                    match = False
                    break
            if match:
                #found possible reflection line
                k = i-1
                l = i+2
                good = True
                while k >=0 and l < len(data[0]):
                    j = 0
                    while j < len(data):
                        if data[j][k] == data[j][l]:
                            j = j+1
                        else:
                            good = False
                            break
                    if good == False:
                        break
                
                    k = k-1
                    l = l+1
            
                if good:
                    #found reflection line (rows)
                    col = col+i+1
                    break
        
            i = i+1
    
    rowTotal = rowTotal+rows
    colTotal = colTotal+col

print(rowTotal)
print(colTotal)
total = colTotal+(rowTotal*100)

print(total)
