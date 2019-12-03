import math

m=[]

with open("input02.txt", "r") as file:
  for line in file:
    m = [int(x) for x in line.split(',')]

#restore the gravity assist program
m[1] = 12
m[2] = 2

for x in range(0, len(m), 4):
  if(m[x] == 99):
    break
  if(m[x] == 1):
    first = m[x+1]
    second = m[x+2]
    third = m[x+3]
    m[third] = m[first] + m[second]
  if(m[x] == 2):
    first = m[x+1]
    second = m[x+2]
    third = m[x+3]
    m[third] = m[first] * m[second]

print(m[0])
