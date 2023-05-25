x = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
y = [(3, 3, 3), (2, 2, 2), (1, 1, 1)]
z = [(2, 2, 2), (3, 3, 3), (4, 4, 4)]
new_list = []
for i in range(len(x)):
    new_list.append(x[i][0] * y[i][1] * z[i][2])
print(new_list)