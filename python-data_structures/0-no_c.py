def no_c(my_string):
    filtered_chars = [char for char in my_string if char.lower() !='c']
    result = '' .join(filtered_chars)
    return result

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is Fun"))


