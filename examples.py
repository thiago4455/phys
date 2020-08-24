from Matrix import Matrix

x = Matrix([
    [2,2],
    [2,2]
])

y = Matrix([
    [1,1],
    [1,1]
])


z = Matrix([
    [3,0,0],
    [3,3,0],
    [3,3,3],
])

print(x+y)  # 3,3
            # 3,3

print(x-1)  # 1,1
            # 1,1

print(x*y)  # 4,4
            # 4,4

print(x*10) # 20,20
            # 20,20

print(x.determinant) # 0
print(z.determinant) # 27

print(~z)   # 3,3,3
            # 0,3,3
            # 0,0,3