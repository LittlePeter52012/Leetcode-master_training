from re import I
from tkinter.messagebox import RETRY
import numpy as np

#TAG1 运用循环计算数组累加结果
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print (sum([2, 4, 6]))

#TAG2 运用递归计算数组累加结果
def sum(list):
    if (list == []):
        return 0
    return list[0] + sum(list[1:])

print(
    sum([2, 4, 6])
)

arr = [1,2,3,4]
#NOTE: "[1:]"指去掉聊表中第1个元素（下标为0）
arr[1:]

#TAG3 编写一个递归函数来计算列表包含的元素书
def count(list):
    if (list == []):
        return 0
    return 1 + count(list[1:])

print(
    count([1,2,3,3])
)

#TAG4 找出列表中最大的数字
#INFO 4.1 运用递归进行计算
def find_max(list):
    if (len(list) == 2):
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(
    find_max([2, 3, 120, 3])
)

#INFO 4.2 运用循环进行计算
def max(list):
    maximum = list[0]
    maximum_index = 0
    for i in range(1, len(list)):
        if list[i] > maximum:
            maximum_index = i
            maximum = list[i]
    return maximum, "index = %d" % (maximum_index)

print(
    max([2, 3, 120, 3])
)

#TAG5 快速排序

def quicksort(array):
    if len(array) < 2:
        return array    # 基线条件：为空或者只包含一个元素的数组是有序的
    else:
        pivot = array[0]    # 选择基准值
        less = [
            i for i in array[1:]
            if i <= pivot
        ] # 由所有小于等于基准值的元素组成的子数组

        greater = [
            i for i in array[1:]
            if i > pivot
        ]   # 由所有大于基准值的元素组成的子数组

        return quicksort(less) + [pivot] + quicksort(greater)

print(
    quicksort(
        [10, 5, 2, 3]
    )
)
