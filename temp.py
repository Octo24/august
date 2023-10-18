def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"{celsius} Celsius to Fahrenheit is {fahrenheit}")

celsius_to_fahrenheit()
print(f"{celsius} Celsius to Fahrenheit is {fahrenheit}")

fahrenheit = 82

fahrenheit_to_celsius()
print(f"{fahrenheit} Fahrenheit to Celsius is {celsius}")

input("how old are you")
