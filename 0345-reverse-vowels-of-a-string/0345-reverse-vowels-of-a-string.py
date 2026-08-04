# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         a=''
#         for i in s:
#             if i in "aeiouAEIOU":
#                 a+=i
#         b=a[::-1]
#         for i in s:
#             if i in "aeiouAEIOU":
#                 for j in b:
#                     i=j
#                     break
                    
class Solution:
    def reverseVowels(self, s: str) -> str:
        # 1. Convert string to a list so we can modify it
        chars = list(s)
        vowels = "aeiouAEIOU"
        
        # 2. Collect all the vowels found in the string
        saved_vowels = []
        for c in s:
            if c in vowels:
                saved_vowels.append(c)
                
        # 3. Put vowels back into the list in reverse order
        for i in range(len(chars)):
            if chars[i] in vowels:
                # .pop() takes the LAST vowel out of our saved list
                chars[i] = saved_vowels.pop()
                
        # 4. Convert the list back into a single string
        return "".join(chars)
