x = int(input("Enter capacity of Jug1: "))
y = int(input("Enter capacity of Jug2: "))
goal = int(input("Enter goal amount: "))

a = 0
b = 0

print("\nJug1\tJug2")

while a != goal:
    if a == 0:
        a = x
    elif b == y:
        b = 0
    else:
        t = min(a, y - b)
        a = a - t
        b = b + t
    print(a, "\t", b)

print(f"\nGoal reached: {goal} liters in Jug1")
