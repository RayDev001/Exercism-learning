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

    total = 0
    n = 1
    
    while n <= 64:
      total = total + square(n)
      n = n + 1
      
    return total
