#TAG1 创建描述这些边的权重的散列表
from concurrent.futures import process


graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# 获取起点的所有邻居
print(
    graph["start"].keys()
)

# 获取这些边的权重
print(
    graph["start"]["a"],"\n",
    graph["start"]["b"]
)

# 添加其他节点及其邻居
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}   # 终点没有任何邻居

#TAG2 创建开销代码
infinity = float("inf")  #python中用"inf"来表示无穷大
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#TAG3 创建存储父节点的散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

#TAG4 创建一个数组，用于记录处理过的节点。对于同一个节点，我们不用处理多次。
processed = []

#TAG5 狄克斯特拉算法的Python代码
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  #遍历所有节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed:    #如果当前节点的开销更低且未处理过，
            lowest_cost = cost  #就将其视为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs) #在未处理的节点中找出开销最小的节点
while node is not None: #这个while循环在所有节点都被处理后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():   #遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: #如果经过当前节点前往邻居更近
            costs[n] = new_cost #更新该邻居的开销
            parents[n] = node   #将该邻居的父节点设置为当前节点
    processed.append(node)  #将当前节点标记为处理过
    node = find_lowest_cost_node(costs) #找出接下来要处理的节点，并循环

print(
    costs,"\n",
    parents
)