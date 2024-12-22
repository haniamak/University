def searchInsert(nums, target):
  l = 0
  r = len(nums) - 1
  while l != r:
    mid = (r + l) // 2
    if nums[mid] ==  target:
      return mid
    if nums[mid] > target:
      r = r - mid
    else:
      l = l + mid
  return l
print(searchInsert([1, 3, 5, 6,], 2))