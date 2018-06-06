# 1. Two Sum
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []

        flag = 0
        for i in range(len(nums)-1):
            # 递归
            a = nums[i]
            b = target - a
            # print(nums[i + 1:])
            if b in nums[i + 1:]:
                # # print('a=%s, b=%s' % (a,b))
                # print(nums[i + 1:])
                # print(nums[i + 1:].index(b))
                flag = 1
                res.append(i)
                res.append(i+(nums[i + 1:].index(b))+1)
                break

        if flag == 0:
            print("error! CAN'T find return list! ")

        return res