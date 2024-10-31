import math

# Given volume
V = 100  # cubic kilometers

# Step 1: Calculate the radius of the sphere
r = (3 * V / (4 * math.pi))**(1/3)
S_sphere = 4 * math.pi * r**2
print("Площадь поверхности шара: ", S_sphere)
print("Радиус сферы:", r)

# Step 2: Set a and b to 0.75 * r, calculate c
a = b = 0.75 * r
c = V / ((4 / 3) * math.pi * a**2)
print("Сжатие элипсоида по x и y: ", a,b)
print("Растижение элипсоида пор оси Z:", c)

# Step 3: Calculate the surface area of the ellipsoid
p = 1.6
S_ellipsoid = 4 * math.pi * (
    ((a * b)**p + (a * c)**p + (b * c)**p) / 3
) ** (1 / p)
print("Пощадь поверхности элипсоида:", S_ellipsoid)
