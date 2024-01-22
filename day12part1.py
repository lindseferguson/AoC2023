input = open("inputday12.txt")
data = input.read()

data = data.splitlines()

lines = []
for line in data:
    lines.append(line.split(" "))

for l in lines:
    nums = l[1].split(",")
    items = len(nums)-1
    for n in nums:
        items = items+int(n)
    
    springs = []
    springs.extend(l[0])
    qmarks = springs.count("?")

    print(qmarks)



#total # must equal sum of all springs 
#. are at least one less than the number of numbers

#print(data)