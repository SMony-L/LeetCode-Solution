def twoSum(nums, target):
    required = {}
    for i in range(len(nums)):
        result = target - nums[i]
        if result in required:
            return [required[result],i]
        else:
            required[nums[i]]=i

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9

    result = twoSum(nums,target)
    print(result)