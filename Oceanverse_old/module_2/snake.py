print("Enter the number of lines and curvature:")
nLines=int(input())
curvature=float(input())

maxSpaces=int((nLines//2)**2*abs(curvature))

for i in range(nLines//2,0,-1):
    spaces=int(i**2*(curvature))
    if curvature<0:
        spaces=maxSpaces-spaces
    print(" "*spaces+"*")

for i in range(nLines//2):
    spaces=int(i**2*(curvature))
    if curvature<0:
        spaces=maxSpaces-spaces
    print(" "*spaces+"*")