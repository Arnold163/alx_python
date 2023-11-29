for i in range(10):
    for x in range(i + 1, 10):
     result = i * 10 + x
     print("{:02d}, ".format(i * 10 + x), end="") 
     if result == 89:
        print(result)
print("\n")