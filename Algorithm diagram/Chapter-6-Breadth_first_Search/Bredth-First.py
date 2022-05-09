#TAG3 广度优先搜索算法-删除重复重复人际关系后的代码:

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = [] 
graph["peggy"] = [] 

from collections import deque

def person_is_seller(name):
    return name[-1] == "m"  #如果函数检查人的名字是以m结尾，则是芒果经销商。

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue: #只要搜索的队列不为空
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(
                    person +  " is a mongo seller"
                )
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")