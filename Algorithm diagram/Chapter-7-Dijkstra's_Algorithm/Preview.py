# 1. 创建有向图的散列表

from tkinter.messagebox import NO


graph = {}
graph["start"] = {}
graph["start"]["A"] = 6
graph["start"]["B"] = 2

graph["A"] = {}
graph["A"]["FIN"] = 1

graph["B"] = {}
graph["B"]["A"] = 3
graph["B"]["FIN"] = 5

graph["FIN"] = {}

# 2. 创建开销散列表
costs = {}
costs["A"] = 6
costs["B"] = 2
Infinity = float("inf")
costs["FIN"] = Infinity

# 3. 创建父列表
parents = {}
parents["A"] = "START"
parents["B"] = "START"
parents["FIN"] = None

for node in costs:
    print(costs[node]) # 打印出的是值

# 4. 创建一个数组用于记录处理过的节点
processed = []

# 5. find lowest cost node
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# 6. Dijkstra's Algorithm
node  = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
