import math

totalFuelRequirement = 0

with open("input01.txt", "r") as file:
  for mass in file: 
    fuel = math.floor(int(mass) / 3) - 2
    totalFuelRequirement += fuel
    while (fuel > 0):
      x = math.floor(fuel / 3) - 2
      if(x <= 0):
        break
      totalFuelRequirement += x
      fuel = x

print(totalFuelRequirement)



