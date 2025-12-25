class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        a=sum(apple)
        capacity.sort(reverse=True)
        i=0

        while a>0:
            a=a-capacity[i]
            i+=1
        return i



        