class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=""
        v=sorted(strs)
        f=v[0]
        l=v[-1]
        for i in range(min(len(f),len(l))):
            if f[i]!=l[i]:
                return a
            a+=f[i]
        return a