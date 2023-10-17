celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"{celsius} Celsius to Fahrenheit is {fahrenheit}")

def celsius_to_fahrenheit():
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_to_fahrenheit()
print(f"{celsius} Celsius to Fahrenheit is {fahrenheit}")

fahrenheit = 82

def fahrenheit_to_celsius():
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit_to_celsius()
print(f"{fahrenheit} Fahrenheit to Celsius is {celsius}")
