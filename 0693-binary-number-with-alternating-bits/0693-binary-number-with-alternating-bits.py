class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
       
        # p=0
        # while(n!=0):
            
        #     a=n&1
        #     if (a==p):
        #         return False
        #     p=a
        #     n=n>>1
        # return True



        # s=[]
        # while(n>0):
        #     a=n>>2
        #     n//=2
        #     s.append(a)
     



        # s=[]
        # while(n>0):
        #     b=n%2
        #     n//=2
        #     s.append(b) #a.insert(0,b)

        # # #a=str(bin(n))
        # for i in range(0,len(s)-1):
        #     if s[i]==s[i+1]:
        #         return False
        # return True
       
       
       
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0
