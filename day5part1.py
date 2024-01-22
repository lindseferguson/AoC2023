input = open("inputday5.txt")

data = input.read()

data = data.splitlines()

#extract seeds
seeds = data[0]
seeds = seeds.replace("seeds: ","")

#extract seed-to-soil map
seedToSoil = data[data.index("seed-to-soil map:"):data.index("soil-to-fertilizer map:")]
seedToSoil.remove("")
seedToSoil.remove("seed-to-soil map:")

soilToFert = data[data.index("soil-to-fertilizer map:"):data.index("fertilizer-to-water map:")]
soilToFert.remove("")
soilToFert.remove("soil-to-fertilizer map:")

fertToWater = data[data.index("fertilizer-to-water map:"):data.index("water-to-light map:")]
fertToWater.remove("")
fertToWater.remove("fertilizer-to-water map:")

waterToLight = data[data.index("water-to-light map:"):data.index("light-to-temperature map:")]
waterToLight.remove("")
waterToLight.remove("water-to-light map:")

lightToTemp = data[data.index("light-to-temperature map:"):data.index("temperature-to-humidity map:")]
lightToTemp.remove("")
lightToTemp.remove("light-to-temperature map:")

tempToHumidity = data[data.index("temperature-to-humidity map:"):data.index("humidity-to-location map:")]
tempToHumidity.remove("")
tempToHumidity.remove("temperature-to-humidity map:")

humidityToLoc = data[data.index("humidity-to-location map:"):]
humidityToLoc.remove("humidity-to-location map:")

seed = seeds.split(" ")


def findItem(start, map):
    items = []
    for s in start:
        ans = ""
        for a in map:
            temp = a.split(" ")
            if int(s) < int(temp[1]):
            #know its not in the map
                continue
            elif int(s) == int(temp[1]):
                ans = temp[0]
                items.append(ans)
            else:
            #bigger than map value
                a = int(temp[2])-1
                if (int(s))<=(int(temp[1])+a):
                #in range
                    num = int(s)-int(temp[1])
                    ans = str(int(temp[0])+num)
                    items.append(ans)
        if ans == "":
            ans = s
            items.append(ans)

    return items


print(len(seed))
soils = findItem(seed, seedToSoil)
print(len(soils))
fertilizer = findItem(soils, soilToFert)
#print(fertilizer)
water = findItem(fertilizer, fertToWater)
#print(water)
light = findItem(water, waterToLight)
#print(light)
temperature = findItem(light, lightToTemp)
#print(temperature)
humidity = findItem(temperature, tempToHumidity)
#print(humidity)
location = findItem(humidity, humidityToLoc)
print(location)
print(min(location))

location = [int(i) for i in location]
print(location)
print(min(location))