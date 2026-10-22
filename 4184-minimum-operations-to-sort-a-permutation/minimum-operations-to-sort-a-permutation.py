class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        asc_order = 0
        dsc_order = 0

        for i in range(1, n):
            asc_order += (nums[i] == (nums[i-1]+1)%n)
            dsc_order += (nums[i-1] == (nums[i]+1)%n)

        if asc_order == n-1 and nums[0] == 0:
            return 0

        if asc_order == n - 1:
            leftRotation = n - nums[0]
            rightRotation = 1 + nums[-1] +1 + 1
            return min(leftRotation,rightRotation)        

        if dsc_order == n - 1:
            left_rotation = n - nums[-1] + 1
            right_Rotation = (nums[0] + 1) % n + 1
            return min(left_rotation, right_Rotation)

        return -1