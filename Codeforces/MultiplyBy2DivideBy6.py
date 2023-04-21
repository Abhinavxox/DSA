def main():
  t = int(input())
  while t > 0:
    n = int(input())
    try:
        print(mulBy2DivBy6(n))
    except:
        print(-1)
    t -= 1

def mulBy2DivBy6(n):
    if n==1:
       return 0
    if n%6==0:
       return 1 + mulBy2DivBy6(n/6)
    if n%6!=0:
       n*=2
       if n%6==0:
          return 2 + mulBy2DivBy6(n/6)
       else:
          return 0+'intentional error'
  
# Driver code
if __name__ == '__main__':
  main()