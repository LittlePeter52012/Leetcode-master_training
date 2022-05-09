#TAG1 准备工作
# 1. 创建一个列表，包含要覆盖的州。

states_needed = set(
    ["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]
)   # 传入一个数组，转换为集合

#NOTE: 结合类似与列表，只是同样的元素只能出现一次，即**集合不能包含重复的元素！**
#举例==================================================
arr = [1, 2, 2, 3, 3, 3]
set(arr)    # 转换为集合后，数字只出现一次。
#======================================================

# 2. 使用散列表创建可供选择的广播台清单

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
# 其中的键为广播台的名称，值为所覆盖的州的集合。

# 3. 使用一个集合来存储最终选择的广播台

final_stations = set()

#TAG2 计算答案

# 1. 遍历所有的广播台，从中选择覆盖了最多的未覆盖州的广播台。并将这个广播台存储在best_station中

'''
best_station = None
states_covered = set()
'''

'''
for station, states_for_station in stations.items():    # items()-以列表返回可遍历的(键，值)元组数组。
    covered = states_needed & states_for_station
    if len(covered) > len(states_covered):
        best_station = station
        states_covered = covered
'''


# for中两个参数用来分别循环第一个键值和第二个键值，如：
for station, states_for_station in stations.items():    
    print(station)
    print(states_for_station)
# ===========================================================

#TAG3 各类集合举例

fruits = set(["avocado", "tomato", "banana"])
vegetables = set(["beets", "carrots", "tomato"])
# 并集
print(fruits | vegetables)
# 交集
print(fruits & vegetables)
# 差集
print(fruits - vegetables)  # 属于水果，但不属于蔬菜
print(vegetables - fruits)  # 属于蔬菜，但不属于水果

#TAG4 回到代码

while states_needed:    # 当states_neede非空的时候
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():    # items()-以列表返回可遍历的(键，值)元组数组。
        # 在for循环结束后将best_station添加到最终的广播台列表中
        covered = states_needed & states_for_station    # 包含当前广播台覆盖的一系列还未覆盖的州
        # 检查该广播台覆盖的州是否比best_station多，如果是，就将best_station设置为当前广播台
        if len(covered) > len(states_covered):  
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)