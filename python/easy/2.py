def c_to_f(temperature):
    """Converts temperature from
    Celsius to Fahrenheit.
    """
    return (temperature * (9/5)) + 32

def f_to_c(temperature):
    """Converts temperature from
    Fahrenheit to Celsius. 
    """
    return (temperature - 32) * (5/9)

if __name__ == '__main__':
    c_to_f(20)
