def no_c(my_string):
    filtered_chars = [char for char in my_string if char.lower() !='c']
    result = '' .join(filtered_chars)
    return result

word = "School"
new_word = no_c(word)




