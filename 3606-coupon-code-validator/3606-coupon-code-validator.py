class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        valid = []
        
        for c, b, a in zip(code, businessLine, isActive):
            if a and b in order and c and all(ch.isalnum() or ch == "_" for ch in c):
                valid.append((b, c))
        
        valid.sort(key=lambda x: (order[x[0]], x[1]))
        return [c for b, c in valid]
