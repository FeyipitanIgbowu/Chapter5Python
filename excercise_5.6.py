def rotate(x, y, z):
    return (z, x, y)

a, b, c = "Feyi", 22, 2000

a, b, c = rotate(a, b, c)
print(a, b, c)

a, b, c = rotate(a, b, c)
print(a, b, c)

a, b, c = rotate(a, b, c)
print(a, b, c)
