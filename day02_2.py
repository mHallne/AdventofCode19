import math

m=[]

with open("input02.txt", "r") as file:
  for line in file:
    m = [int(x) for x in line.split(',')]


for noun in range(0, 99):
  for verb in range(0, 99):
    t = m.copy()
    t[1] = noun
    t[2] = verb

    for x in range(0, len(t), 4):
      if(t[x] == 99):
        break
      if(t[x] == 1):
        first = t[x+1]
        second = t[x+2]
        third = t[x+3]
        t[third] = t[first] + t[second]
      if(t[x] == 2):
        first = t[x+1]
        second = t[x+2]
        third = t[x+3]
        t[third] = t[first] * t[second]

    if(t[0] == 19690720):
      print("Answer: ", 100*noun+verb)
