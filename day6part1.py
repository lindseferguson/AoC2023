input = open("inputday6.txt")
data = input.read()

data = data.splitlines()

times = data[0]
times = times.replace("Time: ", "")
times = times.split(" ")
times = list(filter(None, times))

dist = data[1]
dist = dist.replace("Distance: ", "")
dist = dist.split(" ")
dist = list(filter(None, dist))

j = 0
answers = []
for t in times:
    n = 1
    d = []
    distanceTravelled = dist[j]
    while n <= int(t):
        timeToMove = int(t)-n
        distance = timeToMove*n
        d.append(distance)
        n = n+1
    
    sum = 0
    for i in d:
        if i > int(distanceTravelled):
            sum = sum+1
    answers.append(sum)

    j = j+1

answer = 1
for a in answers:
    answer = answer*a

print(answer)