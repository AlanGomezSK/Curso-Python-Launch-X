#EXERCISE ONE
print("MAKE AND USE list ON PYTHON".title())
planets=["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
i=0
for i in range(len(planets)):
    print(planets[i])
planets.append("Pluton")
print("--------------------------------------")

for i in range(len(planets)):
    print(planets[i])
#EXERCISE NUMBER TWO
print("--------------------------------------")
print("Working with data from a list".title())
planets2 = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'neptune']
question = str(input("¿Givme the name of a planet?"))
question=question.lower()
indexof_planets=(planets2.index(question))
print("the planet that you select is", question)
print("A planet more closer of the sun than the planet you select: ", (planets2[0:indexof_planets]))
print("The planet more far of the sun than the planet you select:", (planets2[indexof_planets+1:]))
