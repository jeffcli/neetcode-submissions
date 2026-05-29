class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort();
        lista = []
        count = 1
        for i in range(1, len(nums)):
            if (nums[i]==nums[i-1]+1):
                count+=1
            elif (nums[i]==nums[i-1]):
                count +=0
            else:
                lista.append(count)
                count = 1
        
        
        lista.append(count)
        return max(lista)