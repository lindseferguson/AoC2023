input = open("inputday15.txt")
data = input.read()

data = data.split(",")
print(data)

total = 0
for item in data:
    print(item)
    cV = 0
    char = []
    char.extend(item)
    
    for c in char:
        ascii_value = ord(c)
        cV = ascii_value+cV
        cV = cV*17
        cV = cV%256


    total = total+cV

print(total)
