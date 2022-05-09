#TAG1 图的实现

from gc import garbage
from re import search

from matplotlib import collections


graph = {}
graph["you"] = [
    "alice", "bob", "claire"
]

print(graph)

# Bigger graph
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = [] 
graph["peggy"] = [] 

print(graph["you"])

#TAG2 广度优先搜索算法的实现

#TODO-1 创建一个队列，python中可以使用deque来创建双端队列
from collections import deque
search_queue = deque()
search_queue += graph["you"]

#TODO-3.1 定义"判断芒果经销商"函数
def person_is_seller(person):
    return name[-1] == "m"  #如果函数检查人的名字是以m结尾，则是芒果经销商。

while search_queue: #语句涵义为：只要队列不为空(判断列表是否为空)
#TODO-2 从队列中弹出一个人
    person = search_queue.popleft() #取出列表中左边第一个人
    #INFO pop: 可以带参数，pop(1)指拿出列表中第2个参数(参数从队列中取消)
    #INFO popleft: 不可以带参数，popleft()指拿出列表中最左边参数(参数从列表中取消)
#TODO-3 判断这个人是否是芒果经销商
    if person_is_seller(person):    #如果是芒果经销商，任务完成
        print(
            person + "is a mango seller!"
        )
        return True
    else:   #如果不是芒果经销商，将这个人的朋友都加入搜索队列
        search_queue += graph[person]
return False

