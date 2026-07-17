class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        l=0



        l=[]
        for i in range(len(nums)):
            p=set(nums[:i+1])
            s=set((nums[i+1:]))
            
            l.append(len(p)-len(s))
        return l