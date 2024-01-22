import copy

input = open("inputday16.txt")
data = input.read()

data = data.splitlines()

input = []

for line in data:
    temp = []
    temp.extend(line)
    input.append(temp)

#print(input)

final = copy.deepcopy(input)
beams = []
direction = "right"

#print(final)
#print(input)

beams.append([direction,0,0])
length = len(input[0])-1

#start on 0,0

def nextSquare (direct, x, y):
    final[x][y] = "#"
    out = []
    if direct == "right":
        col = y+1
        row = x
        if input[row][col] == "." or input[row][col]=="-":
            out.append(["right", row, col])
        if input[row][col] == "\\":
            out.append(["down", row, col])
        if input[row][col] == "/":
            out.append(["up", row, col])
        if input[row][col] == "|":
            out.append(["up", row, col])
            out.append(["down",row, col])

    if direct == "left":
        col = y-1
        row = x
        if input[row][col] == "." or input[row][col]=="-":
            out.append(["left", row, col])
        if input[row][col] == "\\":
            out.append(["up", row, col])
        if input[row][col] == "/":
            out.append(["down", row, col])
        if input[row][col] == "|":
            out.append(["up", row, col])
            out.append(["down",row, col])

    if direct == "up":
        col = y
        row = x-1
        if input[row][col] == "." or input[row][col]=="|":
            out.append(["up", row, col])
        if input[row][col] == "\\":
            out.append(["left", row, col])
        if input[row][col] == "/":
            out.append(["right", row, col])
        if input[row][col] == "-":
            out.append(["left", row, col])
            out.append(["right",row, col])

    if direct == "down":
        col = y
        row = x+1
        if input[row][col] == "." or input[row][col]=="|":
            out.append(["down", row, col])
        if input[row][col] == "\\":
            out.append(["right", row, col])
        if input[row][col] == "/":
            out.append(["left", row, col])
        if input[row][col] == "-":
            out.append(["left", row, col])
            out.append(["right",row, col])
        
    i = 0
    for item in out:
        if item[0]=="right" and item[2] == length:
            final[row][col] = "#"
            out.pop(i)
        if item[0]=="left" and item[2] == 0:
            final[row][col] = "#"
            out.pop(i)
        if item[0]=="up" and item[1] == 0:
            final[row][col] = "#"
            out.pop(i)
        if item[0]=="down" and item[1] == length:
            final[row][col] = "#"
            out.pop(i)
        i = i+1



    return out

previous_count = 0
run = 0

while len(beams)>0:
    temp = []
    for beam in beams:
        t = nextSquare(beam[0], beam[1], beam[2])
        for i in t:
            temp.append(i)
    beams = temp
    run = run+1
    if run == 25000:
        break

print(count)
#print(final)