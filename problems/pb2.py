def max_values(nums):

  max = nums [0]
  for i in nums:
    if i > max:
      max = i
  return max




# Test cases
#print(max_values([4, 7, 2, 8, 10, 9])) # -> [4, 5]
#print(max_values([-5, -2, -1, -11])) # -> [1, 2]