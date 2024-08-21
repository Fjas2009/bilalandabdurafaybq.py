def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
    
print("Welcome to Temperature Conversion\n")
n = 'y'
while n == 'y':
    choice = input('Celsius or Fahrenheit (c/f)? ').lower()
    
    if choice == 'celsius' or choice == 'c':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
        
    elif choice == 'fahrenheit' or choice == 'f':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
        
    else:
        print("Invalid choice.")
        
    n = input("Do you want to continue? Press 'y' for yes and 'n' for no: ").lower()

print("Goodbye!")
