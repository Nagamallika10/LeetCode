class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in nums:
            a=(a^i)&~b
            b=(b^i)&~a
        return a

#         d={}
#         for i in nums:
#             # d[i]=d.get(i,0)+1
#             if i not in d:  #d[i]=d.get(i,0)+1
#                 d[i]=1
#             else:
#                 d[i]+=1
#         for i,j in d.items():
#             if j==1:
#                 return i




        
        