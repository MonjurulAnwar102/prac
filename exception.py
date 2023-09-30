import sys

try:
    x=int(input())
    y=int(input())

except ValueError:
    print("Invalid Input")
    sys.exit(1)



try:

    result=x/y

except ZeroDivisionError:
    print('cannot divide by zeo')
    sys.exit(1)

print(result)