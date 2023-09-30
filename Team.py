x=int(input())
count=0
for _ in range(x):

  a=input().split()
  a=list(map(int,a))

  if sum(a)>=2:
    count+=1

print(count)
        

