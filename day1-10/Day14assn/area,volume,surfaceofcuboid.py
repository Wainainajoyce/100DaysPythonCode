#A program to find the surface area and volume of a cuboid
#Surface area  A=2lw+2lh+2wh
#Volume  V=lwh

#To calculate surface area
length = int(input("Enter the length of cuboid: "))
width = int(input("Enter the width of cuboid: "))
height = int(input("Enter the height of cuboid: "))

def surfaceAreaa(l,w,h):
    surfaceareah = (2*l*w) + (2*l*h) + (2*w*h)
    return surfaceareah
surfaceArea = surfaceAreaa(length,width,height)
print(f"The surface area of the cuboid is {surfaceArea}")

#To calculate volume

def volumee(l,w,h):
    volumeh = l*w*h
    return volumeh
volume = volumee(length,width,height)
print(f"The Volume of the cuboid is {volume}")



