input = open("inputday4.txt")

data = input.read()

data = data.splitlines()

print(data)

answer = 0

for line in data:
    card_num = line[line.find(":")+2:line.find("|")]
    win_num = line[line.find("|")+2:]

    card_num = card_num.split(" ")
    win_num = win_num.split(" ")

    points = 0
    for card in card_num:
        if card.isnumeric():
            for win in win_num:
                if win.isnumeric():
                    if card == win:
                        if points == 0:
                            points = 1
                        else:
                            points = points*2

    answer = answer+points

print(answer)