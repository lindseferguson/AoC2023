input = open("inputday7.txt")
data = input.read()

data = data.splitlines()

letterCards = ["A", "K", "Q", "T"]

#types:
#5K - five of a kind
#4K - four of a kind
#FH - full house
#3K - three of a kind
#2P - 2 pair
#1P - 1 pair
#HC - high card

handTypes = []
handOrdered = []

count = 0
for h in data:
    hSplit = h.split(" ")
    hand = hSplit[0]
    
    cards = list(hand)
    n = 1
    cardsUnique = [cards[0]]

    while n < len(cards):
        match = False
        for cU in cardsUnique:
            if cU == cards[n]:
                match = True
            
        if match == False:
            cardsUnique.append(cards[n])
        n = n+1

    cardCount = []

    for item in cardsUnique:
        cardCount.append(h[0:5].count(item))

    if "J" in cardsUnique:
        #need to reassign Joker
        m = 0
        i = 0
        for card in cardsUnique:
            if card != "J" and cardCount[i] > m:
                m = cardCount[i]
            i = i+1

        i = 0

        maxCards = []
        for cc in cardCount:
            if cc == m and cardsUnique[i] != "J" :
                maxCards.append(cardsUnique[i])

            i = i+1 
        
        if len(maxCards) == 0:
            #all J so reassign to A
            n = 0
            newHand = ""
            while n<5:
                if hand[n] == "J":
                    newHand = newHand+"A"
                else:
                    newHand = newHand+hand[n]
                n = n+1
            #h = newHand+" "+hSplit[1]
            #hand = newHand
        
        elif len(maxCards) == 1:
            #reassign J to maxCard
            n = 0
            newHand = ""
            while n<5:
                if hand[n] == "J":
                    newHand = newHand+maxCards[0]
                else:
                    newHand = newHand+hand[n]
                n = n+1
            #h = newHand+" "+hSplit[1]
            #hand = newHand

        else:
            #multiple max cards, find highest
            m = "0"

            for mC in maxCards:
                
                if mC == "A":
                    m = "A"
                elif mC == "K" and m != "A":
                    m = "K"
                elif mC == "Q" and m!= "A" and m!= "K":
                    m = "K"
                elif mC == "T" and m!= "A" and m!= "K" and m!="Q":
                    m = "T"
                elif m.isnumeric() and mC.isnumeric():
                    if int(mC) > int(m):
                        m = mC
            n = 0
            newHand = ""
            while n<5:
                if hand[n] == "J":
                    newHand = newHand+m
                else:
                    newHand = newHand+hand[n]
                n = n+1
            #h = newHand+" "+hSplit[1]
            #hand = newHand
    else:
        newHand = hand
    
    cards = list(newHand)
    n = 1
    cardsUnique = [cards[0]]

    while n < len(cards):
        match = False
        for cU in cardsUnique:
            if cU == cards[n]:
                match = True
            
        if match == False:
            cardsUnique.append(cards[n])
        n = n+1
    
    cardCount = []

    for item in cardsUnique:
        cardCount.append(newHand.count(item))

    if len(cardsUnique) == 1:
        #5 of a kind
        handTypes.append([h,1])
    elif cardCount.count(4) == 1:
        #4 of a kind
        handTypes.append([h,2])
    elif len(cardsUnique) == 2:
        #Full house
        handTypes.append([h,3])
    elif len(cardsUnique) == 5:
        #high card
        handTypes.append([h,7])
    elif len(cardsUnique) == 4:
        #one pair
        handTypes.append([h,6])
    elif cardCount.count(2) == 2:
        #2 pair
        handTypes.append([h,5])
    else:
        #3 of a kind
        handTypes.append([h,4])
    


handTypes.sort(key=lambda x: x[1])


rank1 = [h for h in handTypes if h[1] == 1]
rank2 = [h for h in handTypes if h[1] == 2]
rank3 = [h for h in handTypes if h[1] == 3]
rank4 = [h for h in handTypes if h[1] == 4]
rank5 = [h for h in handTypes if h[1] == 5]
rank6 = [h for h in handTypes if h[1] == 6]
rank7 = [h for h in handTypes if h[1] == 7]

def order_hands(hand_list):
    rank_order = []
    for h in hand_list:
        hand = h[0]
        i = 0
        #print(rank_order)

        if len(rank_order) == 0:
            rank_order.append(h)
        else:
            insert = False
            for hO in rank_order:
                n = 0
                while n < 5:
                    CL = hand[n]
                    CR = hO[0][n]
                    n = n+1

                    if CL == "J":
                        CL = "0"
                    if CR == "J":
                        CR = "0"
                    if CL == CR:
                        continue
                    elif CL.isnumeric() == False and CR.isnumeric():
                        insert = True
                        break
                    elif CL.isnumeric() and CR.isnumeric() == False:
                        i = i+1
                        break
                    elif CL.isnumeric() and CR.isnumeric():
                        if int(CL)<int(CR):
                            i = i+1
                            break
                        else:
                            insert = True
                            break
                    else:
                        #Both are letter cards (10 through A)
                        numCL = letterCards.index(CL)
                        numCR = letterCards.index(CR)
                        if numCL < numCR:
                            insert = True
                            break
                        elif numCL == numCR:
                            continue
                        else:
                            i = i+1
                            break
                if insert:
                    rank_order.insert(i, h)
                    break
    
            if insert == False:
                rank_order.append(h)
                
                
    return rank_order

rank1_order = order_hands(rank1)
rank2_order = order_hands(rank2)
rank3_order = order_hands(rank3)
rank4_order = order_hands(rank4)
rank5_order = order_hands(rank5)
rank6_order = order_hands(rank6)
rank7_order = order_hands(rank7)




final_order = []
if len(rank1_order)> 0:
    final_order.append(rank1_order)

if len(rank2_order)>0:
    final_order.append(rank2_order)

if len(rank3_order)>0:
    final_order.append(rank3_order)

if len(rank4_order)>0:
    final_order.append(rank4_order)

if len(rank5_order)>0:
    final_order.append(rank5_order)

if len(rank6_order)>0:
    final_order.append(rank6_order)

if len(rank7_order)>0:
    final_order.append(rank7_order)


answer = 0
rank = len(handTypes)

for group in final_order:
    for hand in group:
        h = hand[0]
        point = h.split(" ")
        answer = answer+(int(point[1])*rank)
        rank = rank-1


print(answer)
#print(final_order)

