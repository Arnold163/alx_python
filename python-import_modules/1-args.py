import sys

num_args = len(sys.argv) - 1
if num_args == 0:
    print("0 argument.")
elif num_args == 1:
    print("1 argument:")
else: 
    print("{} argument:" .format(num_args))

for i in range(1, num_args + 1):
    print("{}: {}" .format(i, sys.argv[i]), end="")
    print()

["__main__"]
["__name__"]
