class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # a=left
        # for i in range(left+1,right+1):
        #     a=a&left
        # return left


        
        while(left<right):
            right=right&right-1
        return right