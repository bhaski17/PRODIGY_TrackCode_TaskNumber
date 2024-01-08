def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9 / 5 - 459.67

def convert_temperature(value, unit_from, unit_to):
    if unit_from == "C":
        if unit_to == "F":
            return celsius_to_fahrenheit(value)
        elif unit_to == "K":
            return celsius_to_kelvin(value)
    elif unit_from == "F":
        if unit_to == "C":
            return fahrenheit_to_celsius(value)
        elif unit_to == "K":
            return fahrenheit_to_kelvin(value)
    elif unit_from == "K":
        if unit_to == "C":
            return kelvin_to_celsius(value)
        elif unit_to == "F":
            return kelvin_to_fahrenheit(value)

def main():
    print("Temperature Converter")
    print("Enter 'exit' to end the program.")

    while True:
        try:
            input_str = input("Enter temperature value and units (e.g., '25 C to F'): ")
            if input_str.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            parts = input_str.split()
            if len(parts) == 4 and parts[1].upper() in ["C", "F", "K"] and parts[3].upper() in ["C", "F", "K"] and parts[2].lower() == 'to':
                temperature = float(parts[0])
                unit_from = parts[1].upper()
                unit_to = parts[3].upper()

                result = convert_temperature(temperature, unit_from, unit_to)
                print(f"{temperature} {unit_from} is {result:.2f} {unit_to}")
            else:
                print("Invalid input. Please follow the format: '25 C to F'")
        except ValueError:
            print("Invalid input. Please enter a valid temperature value.")

if __name__ == "__main__":
    main()