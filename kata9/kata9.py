def tanks(tank1,tank2,tank3):
    print(f"""Fuel report
    tank 1:{tank1}%
    tank 2:{tank2}%
    tank 3: {tank3}% 
    And the average of the all fuel is:{(tank1+tank2+tank3)/3}% """)
tanks(100,90,88)

def info_ship(time_travel,destination,passengers,distance,fuel):
    print(f"""
    We are going to have a large travel
    The durution of the travel is {time_travel} Hr
    The destination is {destination}
    The total of passangers is {passengers}
    The distance to pass is {distance} Km
    And we have {fuel}% of fuel 
    We're going {distance/time_travel} km/h """)
info_ship(2,"Mars",250,102000000,90)