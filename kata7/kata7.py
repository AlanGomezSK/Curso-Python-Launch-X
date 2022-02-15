#EXERCISE NUMBER ONE
new_planet= ""
planets=[]

while new_planet.lower() != "done":
    if new_planet:
        planets.append(new_planet)
    new_planet = input("enter a new planet: ")



#EXERCISE NUMBER two
print("this are the planets that you added:")
for i in planets:
    print(i)

