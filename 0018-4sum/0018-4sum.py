class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        i = 0

        while i < n:
            j = i+1
            while j < n:
                l, r = j+1, n-1
                goal = target - nums[i] - nums[j]

                while l < r:
                    if nums[l]+nums[r] == goal:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        while l+1 < n and nums[l+1] == nums[l]: l += 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > goal:
                        r -= 1
                    else:
                        l += 1

                while j+1 < n and nums[j+1] == nums[j]: j += 1
                j += 1
            
            while i+1 < n and nums[i+1] == nums[i]: i += 1
            i += 1
        return ans