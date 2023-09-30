import math
a,b,c=map(int,input().split())


length_flagstone=math.ceil(a/c)
width_flagstone=math.ceil(b/c)

total=width_flagstone*length_flagstone

print(total)