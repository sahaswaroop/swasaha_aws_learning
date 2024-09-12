class Solution:
    def removeElement(self, nums, val):
        k=0
        #res=0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[k]= nums[index]
                k=k+1
        #res=len(nums)-k
        print(nums)
        return k 

sol = Solution()
nums = [0,1,2,2,3,0,4,2] #[0, 1, 3, 0, 4, 0, 4, 2]
val = 2
print(sol.removeElement(nums,val))