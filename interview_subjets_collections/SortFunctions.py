"""
快速排序：分治法把一个list分为两个子串
    1. 从数列中随机挑一个元素，成为基准元素
    2. 重新排序数列，所有元素比基准元素小的房前面，比基准元素大的放后面，相同的随意。在这个分区退出之后，该
       基准元素就会处于数列的中间位置。这个称为分区操作。
    3. 递归的把小于基准元素的子数列和大于基准值元素的子数列排序。
"""
import random
def quick_sort(list, left, right):
    if left >= right:
        return

    low = left
    high = right
    key = list[low]

    while left < right:
        while left < right and list[right] > key:
            right -= 1
        list[left] = list[right]
        while left < right and list[left] < key:
            left += 1
        list[right] = list[left]
    list[right] = key
    quick_sort(list, low, left -1)
    quick_sort(list, left+1, high)


def quick_sort_1(list, left , right):
    if left >= right:
        return

    low = left
    high = right
    key = list[low]

    while left < right:
        while left < right and list[right] > key:
            right -= 1
        list[left] = list[right]
        while left < right and list[left] < key:
            left += 1
        list[right] = list[left]
    list[right] = key

    quick_sort_1(list, low, left -1)
    quick_sort_1(list, left + 1 , high)


if __name__ == '__main__':
    list = [67,2,6,4,8,3,10,7,12,34,56]
    quick_sort_1(list, 0, len(list) - 1)
    print(list)
