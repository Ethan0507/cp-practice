faces = {'Tetrahedron' : 4, 'Cube' : 6, 'Octahedron' : 8, 'Dodecahedron' : 12, 'Icosahedron' : 20}
f = 0

for i in range(int(input())):
    f += faces[input()]

print(f)