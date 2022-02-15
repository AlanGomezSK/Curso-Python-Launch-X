#EXERCISE NUMBER ONE
planet = {
    "name":"mars",
    "moons":2
}
print("The name of the planet is:",planet["name"])
planet["diameter"] = {
    "polar": 6752,
    "equatorial": 6792
}
print("The polar diameter of the planet ",planet["name"],"is ",planet["diameter"]["polar"])

#EXERCISE NUMBER TWO
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
moons = planet_moons.values()
planet_number = len(planet_moons.keys())
total_moons = 0;
for i in moons:
    total_moons=total_moons+i
average=total_moons/planet_number
print("The total of moons in the milky away is:",total_moons)
print("The average of moons out of planets is:",average)