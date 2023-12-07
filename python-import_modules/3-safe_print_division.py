def safe_print_division(a, b):
    
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        return result
test_cases = [
        (10, 2),
        (0, 2),
        (10, 0),
        (0, 0),
        (10, -2)
       
    ]
for a, b in test_cases:
    result = safe_print_division(a, b)

    if result is not None:
        print("Inside result: {:.1f}" .format(result))  
        print("{:d} / {:d} = {:.1f}" .format(a, b, result))  
    else:
         print("Inside result: None")
         print("division by zero - case: a = {} / b = {}" . format(a, b))




    
       # print("inside result: {}" .format(result))

#a = 12
#b = 2

#result =safe_print_division(a, b)
#print("{:d} / {:d} = {}" .format(a, b, result))

#a = 12 
#b = 0
#result = safe_print_division(a, b)
#print("{:d} / {:d} = {}" .format(a, b, result))

#a = 10 
#b = 0
#result = safe_print_division(a, b)
#print("{:d} / {:d} = {}" .format(a, b, result))


