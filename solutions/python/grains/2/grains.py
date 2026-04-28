def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")

    output = 1

    for n in range(number):
        output = output + output
    
    output = output // 2
  
    return output

def total():

    total = 0

    for i in range(64):
        total = total + square(i+1)
      
    return total
