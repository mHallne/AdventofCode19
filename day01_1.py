import math

totalFuelRequirement = 0

with open("input01.txt", "r") as file:
  for mass in file: 
    totalFuelRequirement += math.floor(int(mass) / 3) - 2

print(totalFuelRequirement)

