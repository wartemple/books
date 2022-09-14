# 二分算法基础

[toc]

> 二分查找针对的是一个有序的数据集合，查找思想有点类似分治思想。每次都通过跟区间的中间元素对比，将待查找的区间缩小为之前的一半，直到找到要查找的元素，或者区间被缩小为 0。

### 容易出错的 3 个地方

1. 循环退出条件
   注意是 low<=high，而不是 low < high
2. mid 的取值
   实际上，mid=(low+high)/2 这种写法是有问题的。因为如果 low 和 high 比较大的话，两者之和就有可能会溢出。改进的方法是将 mid 的计算方式写成 low+(high-low)/2
3. low 和 height 的更新
   low=mid+1，high=mid-1。注意这里的 +1 和 -1，如果直接写成 low=mid 或者 high=mid，就可能会发生死循环。比如，当 high=3，low=3 时，如果 a[3]不等于 value，就会导致一直循环不退出。

### 二分查找应用场景的局限性

- 二分查找依赖的是顺序表结构，简单点说就是数组。二分查找算法需要按照下标随机访问元素,链表不支持随机访问。
- 二分查找针对的是有序数据
- 数据量太小不适合二分查找，直接 for 循环就行，但是如果数据之间的比较操作非常耗时，也可采用二分查找，参考电话号的查询（11 个字符串的比较）、
- 数据量太大也不适合二分查找。数组是连续的存储空间，有时无法申请一个 1GB 大小的数组。

### 问题解决

#### 如何在 1000 万个整数中快速查找某个整数？**用二分查找**
    > 散列表、二叉树这些支持快速查找的动态数据结构。你可能会觉得，用散列表和二叉树也可以解决这个问题。实际上是不行的。
    > 而二分查找底层依赖的是数组，除了数据本身之外，不需要额外存储其他信息，是最省内存空间的存储方式，所以刚好能在限定的内存大小下解决这个问题

### 简单代码实现

```python3

二分查找
def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low > high:
        mid = low + (high - low) / 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1
```

# 二分查找进阶
> 默认所有数组都是从小到大进行排序

![进阶问题图](Binary_Search_height.png)
匹配到后进行第二次判断
- ## 查找第一个值等于给定值的元素
> 匹配到后进行判断低一位数是否也为目标值，若为目标值继续进行判断,需要查看临界值0
> 假定数组中的所有元素都一样，如何获取到0
```python3

def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low > high:
        mid = low + (high - low) / 2
        if nums[mid] == target:
            if mid - 1 <= 0:
                return 0
            if nums[mid - 1] != target:
                return mid
            else:
                high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
```
- ## 查找最后一个值等于给定值的元素
> 匹配到后进行判断低一位数是否也为目标值，若为目标值继续进行判断,需要查看临界值0
> 假定数组中的所有元素都一样，如何获取到0
```python3

def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low > high:
        mid = low + (high - low) / 2
        if nums[mid] == target:
            if nums[mid + 1] != target:
                return mid
            elif mid + 1 == 0:
                return 0
            else:
                high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
```
- 查找第一个大于等于给定值的元素
- 查找最后一个小于等于给定值的元素

# 结论
值等于给定值”的二分查找确实不怎么会被用到，
二分查找更适合用在“近似”查找问题（第一个，小于等于大于的数），在这类问题上，二分查找的优势更加明显。
比如今天讲的这几种变体问题，用其他数据结构，比如散列表、二叉树，就比较难实现了。
