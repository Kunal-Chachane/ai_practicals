# Apply the concept of production rules to solve the water jug problem. (A Water Jug
# Problem: You are given two jugs, a 4-gallon one and a 3-gallon one, a pump which
# has unlimited water which you can use to fill the jug, and the ground on which
# water may be poured. Neither jug has any measuring markings on it. How can you
# get exactly 2 gallons of water in the 4-gallon jug?)


def water_jug(jug1, jug2, target):
    if target > max(jug1, jug2):
        print("Target cannot be achieved!")
        return

    x = 0  
    y = 0  

    print("\nSteps:\n")

    while x != target and y != target:
        if x == 0:
            x = jug1
            print(f"Fill Jug1 -> ({x}, {y})")
        elif y == jug2:
            y = 0
            print(f"Empty Jug2 -> ({x}, {y})")
        else:
            transfer = min(x, jug2 - y)
            y += transfer
            x -= transfer
            print(f"Transfer Jug1 -> Jug2 -> ({x}, {y})")

    print("\nTarget Achieved!")

jug1 = int(input("Enter capacity of Jug1: "))
jug2 = int(input("Enter capacity of Jug2: "))
target = int(input("Enter target amount: "))

water_jug(jug1, jug2, target)


