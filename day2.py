input = open("inputday2.txt")

data = input.read()

dataSplit = data.splitlines()

possibleGames = []
answer = 0
for game in dataSplit:
    game = game.replace("Game ","")
    i = game.find(":")
    game_num = game[:i]
    game_only = game.replace(game_num+": ", "")
    results = game_only.split(";")
    
    ok = True
    blue = 0
    green = 0
    red = 0

    for r in results:
        dice = r.split(",")
        
        for d in dice:
            d = d.strip()

            if "blue" in d:
                num = int(d.replace(" blue", ""))
                if num > blue:
                    blue = num
            
            if "green" in d:
                num = int(d.replace(" green", ""))
                if num > green:
                    green = num

            if "red" in d:
                num = int(d.replace(" red",""))
                if num > red:
                    red = num

    power = red*green*blue
    answer = answer+int(power)

print(answer)
