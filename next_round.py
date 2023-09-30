n,k=map(int,input().split())
score=list(map(int,input().split()))
count=0
k_score=score[k-1]
for i in score:
    

    if i>=k_score and i > 0:
        count +=1

print(count)