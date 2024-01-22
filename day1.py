input = open("inputday1.txt")

data = input.read()

dataSplit = data.splitlines()

finalNum = []

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in dataSplit:
    temp = list(line)
    a = 'blank'
    b = 'blank'
    for x in temp:
        if x.isnumeric():
            if a == 'blank':
                a = x
                a_pos = line.find(x)
            else:
                b = x
                b_pos = line.rfind(x)

    num_pos = []
    for num in nums:
        pos = line.find(num)
        num_pos.append(pos)

    num_pos_reverse = []
    for num in nums:
        pos = line.rfind(num)
        num_pos_reverse.append(pos)
    

    if a == 'blank':
        a_pos = min([value for value in num_pos if value != -1])
        temp = (nums[num_pos.index(a_pos)])
        a = str(nums.index(temp)+1)
    if b == 'blank':
        b_pos = a_pos
        b = a

    i = 1

    for pos in num_pos:
        
        if pos < a_pos and pos != -1:
            a_pos = pos
            a = str(i)
        i = i+1
    i = 1
    for pos_rev in num_pos_reverse:
        if pos_rev > b_pos and pos_rev != -1:
            b_pos = pos_rev
            b = str(i)
        i = i+1

    print(a)
    print(b)
    print(line)
    print(num_pos) 
    print(num_pos_reverse)
   
   
    finalNum.append(a+b)
answer = 0
for a in finalNum:
    answer = answer + int(a)

print(answer)
