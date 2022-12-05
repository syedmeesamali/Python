c = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
val = []
lil = []
for i in range(3):
    lil.append(i)
    val.append(lil)

for i in range(3):
    for j in range(3):
        val[i][j] = (c[i][j] + d[i][j])
print(val)