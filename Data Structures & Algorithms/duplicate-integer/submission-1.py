class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_intergers = set()
        for i in range(len(nums)):
            if nums[i] in seen_intergers:
                return True
            else:
                seen_intergers.add(nums[i])
        return False
