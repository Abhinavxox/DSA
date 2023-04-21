def YoungPhysicist():
  t = int(input())
  arr = [0,0,0]
  for i in range(t):
    a = list(map(int, input().split(' ')))
    arr = [sum(i) for i in zip(arr, a)]
  if arr[0]==arr[1]==arr[2]==0:
    print('YES')
  else:
    print('NO')

# Driver code
if __name__ == '__main__':
  YoungPhysicist()