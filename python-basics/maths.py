#Name : Cyril Baraka 
#Date : 13/02/2026
#Program to carry out mathematical operations
import math
number=-16.9

print(abs(number))
print(math.ceil(number))

x=60 #radians
y=math.degrees (x) #degrees

print(x),(y)

angle_radians=60
angle_degree=angle_radians/180
print(math.cos(angle_radians))
print(math.sin(angle_radians))
print(math.tan(angle_radians))

print(angle_degree)

print(math.cos(angle_degree))
print(math.sin(angle_degree))
print(math.tan(angle_degree))

print(min(3,4))
print(max(3,4))

print(math.sqrt(144))

print(25**2) #25 raised to the power of two
print(3**3) #3 raised to the power of three




# Sine, cosine, and tangent for even angles (degrees) between 0 and 180
for deg in range(0, 181, 2):
    rad = math.radians(deg)
    sin_val = math.sin(rad)
    cos_val = math.cos(rad)
    tan_val = math.tan(rad)
    print(f"{deg:3d}  sin={sin_val:.6f}  cos={cos_val:.6f}  tan={tan_val:.6f}")
