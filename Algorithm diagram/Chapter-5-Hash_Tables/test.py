#TAG1 散列表在pyhton中的实现为-"dict"(字典)
from sympy import true


book = dict()

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49
print(book)
print(
    book["avocado"]
)

#TAG2.1 散列表的应用-查找
phone_book = dict()
# or phone_book = {} 两者皆可
phone_book["jenny"] = 8675309
phone_book["emergency"] = 110

print(
    phone_book["jenny"]
)

#TAG2.2 散列表的应用-防止重复
vote = {}
value = vote.get("tom") # 如果"tom"在散列表中，函数get将返回True，否则将返回None(get函数默认为None)。

def check_voter(name):
    if vote.get(name):
        print("Kick them out!")
    else:
        vote[name] = True
        print("Let them vote!")

check_voter("tom")
check_voter("mick")
check_voter("tom")
print(vote)

#TAG2.3 散列表的应用-防止重复
cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        cache[url] = data
        return data