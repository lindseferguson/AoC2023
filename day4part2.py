input = open("inputday4.txt")

data = input.read()

data = data.splitlines()

answer = 0
i = 1
final = []
while i <= len(data):
    final.append([i,0,1])
    i = i+1
j = 0
for line in data:
    card_num = line[line.find(":")+2:line.find("|")]
    win_num = line[line.find("|")+2:]

    card_num = card_num.split(" ")
    win_num = win_num.split(" ")

    points = 0
    wins = 0
    for card in card_num:
        if card.isnumeric():
            for win in win_num:
                if win.isnumeric():
                    if card == win:
                        if points == 0:
                            points = 1
                        else:
                            points = points*2
                        wins = wins+1

    #loop and add to the total times that card gets pointed
    repeat = final[j][2]
    print(repeat)
    if wins > 0:
        n = 1
        while n <= wins and j+n < len(final):
            final[j+n][2] = final[j+n][2]+final[j][2]
            n = n+1
    

    j = j+1

for l in final:
    answer = l[2]+answer

print(answer)

