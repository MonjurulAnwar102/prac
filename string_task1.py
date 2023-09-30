x=input()

y=""


vowels=set("AEIOUaeiou")


for i in x:
    if i in vowels:
        continue

    y+="."+i.lower()

print(y)
