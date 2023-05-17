# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
# For example:
# time = 3 ----> litres = 1
# time = 6.7---> litres = 3
# time = 11.8--> litres = 5


def litres(time):

    if time >= 1:
        if time % 1 == 0:
            litres = int(time * 0.5)
            
        elif time % 1 != 0 and time < 1:
            litres = 0 
        else:
            litres = int(time // 1)
    else:
        litres = 0

    return litres

print(litres(1.4)) 


#CORRECT SOLUTION:

def litres(time):
    water = time*0.5
    water = int(water)
    
    return water