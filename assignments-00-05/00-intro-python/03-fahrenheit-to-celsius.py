def main():
    farenheit_value = float(input("Enter temperature in Fahrenheit: "))
    value_into_celcius = (farenheit_value - 32) * 5.0/9.0
    print(f"Temperature: {farenheit_value}F = {value_into_celcius}C")
main()