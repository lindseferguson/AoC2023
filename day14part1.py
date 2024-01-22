input = open("inputday14.txt")
data = input.read()

data = data.splitlines()

j = 0
while j < len(data[0]):
    i = 1
    while i < len(data):    
        if data[i][j] == "O":
            k = i-1
            while k >=0:
                if data[k][j] == ".":
                    if k == 0:
                        temp = list(data[k])
                        temp[j] = "O"
                        data[k] = "".join(temp)

                    temp = list(data[i])
                    temp[j] = "."
                    data[i] = "".join(temp)
                else:
                    temp = list(data[k+1])
                    temp[j] = "O"
                    data[k+1] = "".join(temp)
                    break
            
                k = k-1

        i = i+1
    
    j = j+1

total = 0
count = len(data)
for d in data:
    num = d.count("O")
    total = total + num*count
    count = count-1

print(total)


