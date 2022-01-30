import queue


def reverseFirstK(q, k):
    # Implement Your Code Here
    if k == 0:
        return
    first = q.get()
    reverseFirstK(q, k - 1)
    q.put(first)


from sys import setrecursionlimit

setrecursionlimit(11000)
n, k = map(int, input().split())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
    q.put(ele)

reverseFirstK(q, k)
count = 0
h = n - k
while (count < h):
    q.put(q.get())
    count += 1
while (q.qsize() > 0):
    print(q.get(), end=" ")
    n -= 1
