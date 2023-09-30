
s = input()

numbers = s.split("+")


numbers = sorted(map(int, numbers))


result = "+".join(map(str, numbers))

print(result)
