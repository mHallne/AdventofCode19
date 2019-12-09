import shapely
import matplotlib.pyplot as plt
import sys
from shapely.geometry import LineString

m1=[]
m2=[]
curX, curY, newX, newY, count, steps = 0, 0, 0, 0, 0, 0
lowest = sys.maxsize

# Read and store paths
with open("input03.txt", "r") as file:
  for line in file:
    m1.append([])
    m2.append([])
    m2[count].append(0)
    for x in line.split(','):
      steps = steps + int(x[1:])
      if(x[0] == 'R'):
        newX = curX + int(x[1:])
        newY = curY
      elif(x[0] == 'L'):
        newX = curX - int(x[1:])
        newY = curY
      elif(x[0] == 'U'):
        newY = curY + int(x[1:])
        newX = curX
      else:
        newY = curY - int(x[1:])
        newX = curX

      m1[count].append(([curX, curY], [newX, newY]))
      m2[count].append(steps)
      
      curX, curY = newX, newY
    curX, curY, newX, newY, steps = 0, 0, 0, 0, 0
    count += 1

# Check for overlap
for i, x in enumerate(m1[0]):
  for j, y in enumerate(m1[1]):
    # plt.plot((x[0][0], x[1][0]), (x[0][1], x[1][1]), color="green")
    # plt.plot((y[0][0], y[1][0]), (y[0][1], y[1][1]), color="red")

    line1 = LineString(x)
    line2 = LineString(y)

    int_pt = line1.intersection(line2)
    if(int_pt):
      if(int_pt.x != 0 and int_pt.y != 0):
        # Print intersection
        # plt.plot(int_pt.x, int_pt.y, "bo")

        d1 = abs(x[0][0] - int_pt.x)
        d2 = abs(x[0][1] - int_pt.y)
        d3 = abs(y[0][0] - int_pt.x)
        d4 = abs(y[0][1] - int_pt.y)

        # Steps
        steps = m2[0][i] + m2[1][j] + d1 + d2 + d3 + d4

        if steps < lowest:
          lowest = steps

print(lowest)
