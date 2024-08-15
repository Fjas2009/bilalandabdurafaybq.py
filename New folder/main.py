def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
choice = input('celsius or fahrenhiet ')
if choice == 'celsius' or 'c':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == 'fahrenhiet' or 'f':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid choice. ")