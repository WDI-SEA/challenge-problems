def heightChecker(heights):
  expected = heights.copy()
  expected.sort()
  mismatch = 0

  print(f'{heights}\n{expected}')

  for i, height in enumerate(heights):
    if height != expected[i]: mismatch += 1

  return mismatch

heights = [1,1,4,2,1,3]
print(heightChecker(heights))