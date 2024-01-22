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



time = ""
for t in times:
    time = time+t

distance = ""
for d in dist:
    distance = distance+d


j = 0
answers = []

n = 1
d = []
while n <= int(time):
    timeToMove = int(time)-n
    d.append(timeToMove*n)
    n = n+1

#print(d)
    
sum = 0
for i in d:
    if i > int(distance):
        sum = sum+1
    
print(sum)