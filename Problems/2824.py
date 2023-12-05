    def countPairs(self, nums, target):
        l = 0
        count = 0
        r = 0
        if len(nums) == 1:
            return -1
        else:
            while(l<len(nums)-1):
                r= l+1
                while(r < len(nums)):
                    if nums[l] + nums[r] < target:
                        count+=1
                    r = r+1
                l =l+1
        return count

