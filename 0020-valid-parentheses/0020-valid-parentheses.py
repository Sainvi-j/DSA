class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        hashmap = {')':'(', '}':'{', ']':'['}

        for ele in s:
            if stack and (ele in hashmap and stack  [-1] == hashmap[ele]):
                stack.pop()
            else:
                stack.append(ele)
        return not stack 
        