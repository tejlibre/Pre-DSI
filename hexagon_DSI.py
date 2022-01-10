import matplotlib.pyplot as plt
import math, random

#1. Make a Hexagon

# Hexagon vertices coodinates array
hexagon = []

#Set radius of circumcircle Centered at [0, 0]
#length of a side =  2*R
R = 1

# x and y coordinates of vertices
for n in range(0,6):
  x = R*math.cos(math.radians(90+n*60))
  y = R*math.sin(math.radians(90+n*60))
  hexagon.append([x,y])

# add the first vertex to complete polygon
hexagon.append(hexagon[0])

# Convert to a list
xs, ys = zip(*hexagon)

plt.figure(figsize=(7,7))
plt.plot(xs,ys,'k')


def pick_point(A,B,C):
  """
  Function for uniformly sampling a point P(xp,yp) in a triangle
  using algo from https://www.cs.princeton.edu/~funk/tog02.pdf
  P = (1 − √r1) A + √r1(1 − r2) B + √r1r2 C
  """
  r1 = random.random()
  r2 = random.random()

  r1sq = math.sqrt(r1)
  xp = (1.0 - r1sq) * A[0] + r1sq * (1.0 - r2) * B[0] + r1sq * r2 * C[0]
  yp = (1.0 - r1sq) * A[1] + r1sq * (1.0 - r2) * B[1] + r1sq * r2 * C[1]

  return (xp,yp)


def pick_vertices(hexagon):
  """
  Function to pick two adjacent vertices "randomly"
  from the hexagon polygon
  """
  i = random.randrange(0,6)
  v1 = hexagon[i]
  v2 = hexagon[i+1]

  return(v1,v2)


#2. Pick a random point
#2.1 Pick a random triangle A, B, C formed by edges of hexagon and center of hexagon
A, B = pick_vertices(hexagon)
C = [0.,0.]

#2.2 Pick a random point in one of 6 triangles ABC selected at random above
xp,yp = pick_point(A,B,C)

#2.3 Save random point P
points=[]
P = [xp,yp]
points.append(P)

#3. Make a new triangle T formed from new set of adjacent vertices A,B and random point P(xp,yp)
A, B = pick_vertices(hexagon)

#4. Find centroid of triangle ABP

def centroid(A,B,P):
  xt = (A[0]+B[0]+P[0]) / 3.
  yt = (A[1]+B[1]+P[1]) / 3.
  return(xt,yt)

T = centroid(A,B,P)
points.append(T)

# 5. use centroid as random point P and repeat for 10,000
for i in range(100000):
  A, B = pick_vertices(hexagon)
  T = centroid(A,B,T)
  points.append(T)

plt.scatter(*zip(*points), s=0.02)
plt.show()

# Fractal pattern of hexagon



