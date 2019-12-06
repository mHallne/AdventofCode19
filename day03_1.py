import shapely
import matplotlib.pyplot as plt
import sys
from shapely.geometry import LineString, Point

m1=[]
curX, curY, newX, newY, count = 0, 0, 0, 0, 0
lowest = sys.maxsize

# Read and store paths
with open("input03.txt", "r") as file:
  for line in file:
    m1.append([])
    for x in line.split(','):
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
      
      curX, curY = newX, newY
    curX, curY, newX, newY = 0, 0, 0, 0
    count += 1

# Check for overlap
for x in m1[0]:
  for y in m1[1]:
    # plt.plot((x[0][0], x[1][0]), (x[0][1], x[1][1]), color="green")
    # plt.plot((y[0][0], y[1][0]), (y[0][1], y[1][1]), color="red")

    line1 = LineString(x)
    line2 = LineString(y)

    int_pt = line1.intersection(line2)
    if(int_pt):
      if(int_pt.x != 0 and int_pt.y != 0):
        m = int(abs(int_pt.x) + abs(int_pt.y))
        if m < lowest:
          lowest = m

# plt.show()
print(lowest)
