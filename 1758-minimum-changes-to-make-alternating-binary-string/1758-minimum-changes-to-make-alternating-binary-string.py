class Solution:
    def minOperations(self, s: str) -> int:
        return min(q:=sum(map(ne,s,cycle('01'))),len(s)-q)