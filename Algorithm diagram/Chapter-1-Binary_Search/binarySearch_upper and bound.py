class Solution:
    def minArray(self, numbers: list[int], target: int) -> int:
        left = 0
        right = len(numbers)
        while left < right:
            mid = left + (right - left) // 2
            if numbers[mid] == target:
                right = mid
            elif numbers[mid] < target:
                left = mid + 1
            elif numbers[mid] > target:
                right = mid

        if left >= len(numbers) or numbers[left] != target:
            return -1
        return left

    def maxArray(self, numbers: list[int], target: int) -> int:
        left = 0
        right = len(numbers)
        while left < right:
            mid = left + (right - left) // 2
            if target > numbers[mid]:
                left = mid + 1
            elif target < numbers[mid]:
                right = mid
            elif target == numbers[mid]:
                left = mid + 1
        if left <= 0 or numbers[left - 1] != target:
            return -1
        return left - 1


test = Solution()
# test.minArray([1,2,3,3,3,4], 9)
test.maxArray([1, 2, 3, 3, 3, 5], 3)
