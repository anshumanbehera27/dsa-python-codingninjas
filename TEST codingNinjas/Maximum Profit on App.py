def maximumProfit(arr):
  arr.sort()
  m = 0
  num = len(arr)
  for i in arr:
    if m < i*num:
      m = i*num
    num = num - 1
  return m

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)
