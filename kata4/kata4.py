#SECOND EXERCISE-----------------------------------------------------------------------------------
text= """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
paragraphs=text.split(".")

words=["average", "temperature", "distance"]
for txt in paragraphs:
    for word in words:
        if word in txt:
            print(txt.replace(" C", " Celsius"))
            break
# SECOND EXERCISE---------------------------------------------------------------------------------------------------------
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"
the_title = 'The gravity, the awesome force of the space'
facts=(f"the gravity in the planet {planet} is {gravity*1000} and around of the earth is where the {name} is")
template =f"-------------------------------------------------------------------------\n{the_title.title()}\n{facts}\n-------------------------------------------------------------------------"
print(template)
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
new_template=f"{the_title.title()}\nTop 10 things about {nombre}\n1.The planet {planeta}have one gravity of {gravedad*1000}"
print(new_template.format(nombre=name, gravedad=gravity, planeta=planet))

