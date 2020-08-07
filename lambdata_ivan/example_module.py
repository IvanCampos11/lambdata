def fibonacci(num): 
    if num<0: 
        print("Make it a positive number") 
    elif num==1: 
        return 0
    elif num==2: 
        return 1
    else: 
        return fibonacci(num-1)+fibonacci(num-2)