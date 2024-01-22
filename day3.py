input = open("inputday3.txt")

data = input.read()

#keep everything as an array, look for the first number then check 
#all the possible adjacent elements to see if its not numeric and not .

data = data.splitlines()

all_nums = []
line_nums = []
i = 0
answer = 0
for line in data:
    elements = list(line)
    num = ""
    include = False
    n = 0
    for e in elements:
        if e.isnumeric():
            num = num+e
            #check to see if symbol nearby
            if (n-1) >=0:
                if elements[n-1] != "." and elements[n-1].isnumeric() == False:
                    #value is a symbol
                    include = True
            if (n+1) < len(elements):
                if elements[n+1] != "." and elements[n+1].isnumeric() == False:
                    include = True
            if (i-1) >=0:
                line_above = list(data[i-1])
                if line_above[n] != "." and line_above[n].isnumeric() == False:
                    include= True
                if (n-1)>=0:
                    if line_above[n-1] != "." and line_above[n-1].isnumeric() == False:
                        include = True
                if (n+1) < len(elements):
                    if line_above[n+1] != "." and line_above[n+1].isnumeric() == False:
                        include = True
            if (i+1) < len(data):
                line_below = list(data[i+1])
                if line_below[n] != "." and line_below[n].isnumeric() == False:
                    include= True
                if (n-1) >=0:
                    if line_below[n-1] != "." and line_below[n-1].isnumeric() == False:
                        include = True
                if n+1 < len(elements):
                    if line_below[n+1] != "." and line_below[n+1].isnumeric() == False:
                        include = True
        else:
            #e is either symbol or period
            if len(num) != 0:
                if include:
                    answer = answer+int(num)
                    print(num)
                    include = False
                line_nums.append(num)
                num = ""
        if len(num) != 0 and n+1 == len(elements):
            if include:
                    answer = answer+int(num)
                    print(num)
                    include = False
            line_nums.append(num)
            num = ""
        
        n = n+1
    i = i+1

    all_nums.append(line_nums)
    line_nums = []

print(answer)

