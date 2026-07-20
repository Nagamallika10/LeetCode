class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # j=0
        # s=sorted(nums)
        # for i in s:
        #     if i==j:
        #         j+=1
        #     else:
        #         return j

        for i in range(len(nums)+1):
            if i not in nums:
                return i


        # a=0
        # for i in range(1,len(nums)+1):
        #     a^=i
        # for j in nums:
        #     a^=j
        # return a    


        # l=len(nums)
        # s=(l*(l+1))//2
        # s1=sum(nums)
        # return s-s1