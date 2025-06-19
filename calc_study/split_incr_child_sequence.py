'''
以下是关于 “拆分递增子序列” 问题的详细分析与 Python 实现。该问题常见于面试题中，例如 LeetCode 659 题 “分割数组为连续子序列”。

问题描述
给定一个按升序排列的整数数组 nums，判断是否能将其拆分为一个或多个子序列，使得每个子序列都是至少长度为 3 的连续递增序列（即每个子序列中的元素连续递增且长度≥3）。
示例：
1、输入：nums = [1,2,3,3,4,5]
    输出：True
    解释：可拆分为 [1,2,3] 和 [3,4,5]。
2、输入：nums = [1,2,3,3,4,4,5,5]
    输出：True
    解释：可拆分为 [1,2,3,4,5] 和 [3,4,5]。
3、输入：nums = [1,2,3,4,4,5]
    输出：False
    解释：无法拆分为长度≥3 的连续子序列。
算法思路
使用贪心策略，通过两个哈希表实现：
1、计数表 count：记录每个数的剩余次数。
2、结尾表 tails：记录以某个数结尾的连续子序列的数量。
步骤：
1、统计元素频率：遍历数组，用 count 记录每个数的出现次数。
2、遍历数组：对每个数 x，检查：
    是否能加入现有子序列（即检查 tails[x-1] 是否存在）。
    是否能作为新子序列的起点（即检查 x+1 和 x+2 是否有剩余次数）。
3、动态调整：根据上述条件更新 count 和 tails。
'''


#拆分递增子序列
from collections import defaultdict


def isPossible(nums: list[int]) -> bool:
    # 统计每个数的出现次数
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    # 记录以某个数结尾的连续子序列的数量
    tails = defaultdict(int)
    for num in nums:
        # 如果当前数已经用完，跳过
        if count[num] == 0:
            continue
        # 情况1：加入现有子序列
        if tails.get(num - 1, 0) > 0:
            tails[num - 1] -= 1  # 现有子序列少一个以num-1结尾
            tails[num] += 1  # 新增一个以num结尾的子序列
            count[num] -= 1  # 消耗一个num
        # 情况2：作为新子序列的起点
        elif count.get(num + 1, 0) > 0 and count.get(num + 2, 0) > 0:
            count[num] -= 1  # 消耗一个num
            count[num + 1] -= 1  # 消耗一个num+1
            count[num + 2] -= 1  # 消耗一个num+2
            tails[num + 2] += 1  # 新增一个以num+2结尾的子序列
        # 无法满足条件
        else:
            return False
    return True


# 测试示例
if __name__ == '__main__':
    print(isPossible([1, 2, 3, 3, 4, 5]))  # 输出: True
    print(isPossible([1, 2, 3, 3, 4, 4, 5, 5]))  # 输出: True
    print(isPossible([1, 2, 3, 4, 4, 5]))  # 输出: False
'''
复杂度分析
1、时间复杂度：O (n)，其中 n 是数组长度。需遍历数组两次。
2、空间复杂度：O (n)，主要用于存储 count 和 tails。
关键逻辑解释
1、优先加入现有子序列：通过 tails[num-1] 判断能否扩展现有子序列，确保子序列尽可能长。
2、创建新子序列：当无法扩展现有子序列时，尝试创建长度为 3 的新子序列（检查 num+1 和 num+2）。
3、无法满足条件：若既不能扩展现有子序列，也不能创建新子序列，则返回 False。

该算法通过贪心策略确保每个元素都被合理利用，最终判断是否能拆分出符合条件的子序列。
'''
