class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        ans = 0
        n = len(ages)

        for i, age in enumerate(ages):
            if age < 15:
                continue

            low = bisect.bisect_right(ages, 0.5 * age + 7)
            high = bisect.bisect_right(ages, age) - 1

            ans += max(0, high - low)

        return ans
