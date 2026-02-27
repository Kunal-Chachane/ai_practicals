n = 3
square = []

print("Enter 3x3 matrix values:")

for i in range(n):
    row = list(map(int, input().split()))
    square.append(row)

magic_sum = sum(square[0])

row_check = True
for i in range(n):
    if sum(square[i]) != magic_sum:
        row_check = False

col_check = True
for j in range(n):
    col_sum = 0
    for i in range(n):
        col_sum += square[i][j]
    if col_sum != magic_sum:
        col_check = False

diag1 = 0
diag2 = 0
for i in range(n):
    diag1 += square[i][i]
    diag2 += square[i][n - i - 1]

if row_check and col_check and diag1 == magic_sum and diag2 == magic_sum:
    print("Magic Square")
else:
    print("Not a Magic Square")