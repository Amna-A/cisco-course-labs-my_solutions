# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def l100kmtompg(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons



def mpgtol100km(miles):
    km=(miles*1609.344)/1000
    liters = km /3.785411784
    return liters/100*km
       
    

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))

#A car's fuel consumption may be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.
# In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.
# Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

#1 American mile = 1609.344 metres;
# 1 American gallon = 3.785411784 litres.