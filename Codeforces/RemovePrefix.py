def RemovePrefix():
  t = int(input())
  while t > 0:
    n = int(input()) 
    a = list(map(int, input().split(' ')))
    if(n==1):
      print(0)
      t -= 1
      continue
    se = set()
    ans = n
    for i in range(n-1, -1, -1):
      if a[i] in se:
        break
      ans -= 1
      se.add(a[i])
    print(ans)
    t -= 1

# Driver code
if __name__ == '__main__':
  RemovePrefix()