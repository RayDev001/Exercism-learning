def is_armstrong_number(number):
    s_num = str(number)
    exponente = len(s_num)
    
    suma = sum(int(digito) ** exponente for digito in s_num)
    
    return suma == number
