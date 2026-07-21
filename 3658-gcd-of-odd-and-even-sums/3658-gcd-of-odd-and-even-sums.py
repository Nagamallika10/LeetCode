class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        a=n*(n+1)
        b=n**2
        l=max(a,b)
        m=0
        for i in range(1,l):
            if a%i==0 and b%i==0:
                if m<i:
                    m=i
        return m