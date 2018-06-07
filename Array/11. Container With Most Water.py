class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        11. Container With Most Water 
        注意时间复杂度！弄两个循环做穷举，会让时间变长，导致不能通过测试！
        """

        # 方案1 可以通过，但是速度太慢了，测试通过不了
        # rtype = 0
        # print(height)
        # for i in range(len(height)-1):
        #     a1 = height[i]
        #     a2_list = height[i+1:]
        #     # print("a1=%s||a2_list=%s"%(a1, a2_list))
		#
        #     for j in range(len(a2_list)):
        #         # j = i + a2_list.index(a2) + 1
        #         a2 = a2_list[j]
        #         # print("a2=%s|++|j=%s" % (a2, j))
        #         temp = (j+1)*min(a2,a1)
        #         if temp > rtype:
        #             rtype = temp
        #             print("rtype=%s|++++|a1=%s||a2=%s||i=%s||j=%s"%(rtype, a1, a2, i+1, j+2))

        # 方案2 善于利用指针！一头一尾，向中间靠拢，而不是穷举
        rtype = 0
        print(height)

        a_start = 0
        a_end = len(height)-1
        temp = a_end - a_start
        print("%s||%s" % (temp, height[a_end]))
        while a_start < a_end:
            temp = (a_end - a_start) * min(height[a_start], height[a_end])
            if temp > rtype:
                rtype = temp
            if height[a_start]> height[a_end]:
                a_end = a_end - 1
            else:
                a_start = a_start +1


        return rtype