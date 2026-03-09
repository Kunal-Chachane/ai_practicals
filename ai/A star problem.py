graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    heuristic[node] = int(input("Enter heuristic value: "))
    graph[node] = {}

e = int(input("Enter number of edges: "))

for i in range(e):
    u = input("From node: ")
    v = input("To node: ")
    cost = int(input("Cost: "))
    graph[u][v] = cost

start = input("Enter start node: ")
goal = input("Enter goal node: ")

def a_star(start, goal):
    open_list = [start]
    closed_list = []
    g = {start: 0}
    parent = {start: start}

    while open_list:
        current = min(open_list, key=lambda x: g[x] + heuristic[x])
        print("Current:", current)

        if current == goal:
            path = []
            while parent[current] != current:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            print("Path:", path)
            print("Total Cost:", g[goal])
            return

        open_list.remove(current)
        closed_list.append(current)

        for neighbor in graph[current]:
            cost = g[current] + graph[current][neighbor]

            if neighbor not in open_list and neighbor not in closed_list:
                open_list.append(neighbor)
                parent[neighbor] = current
                g[neighbor] = cost
            elif cost < g.get(neighbor, float('inf')):
                g[neighbor] = cost
                parent[neighbor] = current
                if neighbor in closed_list:
                    closed_list.remove(neighbor)
                    open_list.append(neighbor)

    print("No path found")

a_star(start, goal)