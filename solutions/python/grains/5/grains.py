def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")

    output = 1

    while number > 0:
        output = output + output
        number = number - 1
    
    output = output // 2
  
    return output

def total():
    output = 0
    
    for i in range(64):
        output = output + square(i + 1)
      
    return output