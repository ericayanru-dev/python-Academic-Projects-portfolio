import math

def windchill(T, V):
    """
    Calculate the wind chill based on temperature (F) and wind speed (mph).
    Formula is valid for T <= 50°F and V > 3 mph.
    """
    return 35.74 + 0.6215 * T - 35.75 * (V**0.16) + 0.4275 * T * (V**0.16)

def celsius_to_fahrenheit(C):
    """Convert Celsius to Fahrenheit."""
    return C * (9 / 5) + 32

def main():
    while True:
        try:
            temperature = float(input("What is the temperature? "))
        except ValueError:
            print("Please enter a valid number for temperature.")
            continue

        unit = input("Fahrenheit or Celsius (F/C)? ").strip().lower()

        if unit in ["f", "fahrenheit"]:
            temp_f = temperature
        elif unit in ["c", "celsius"]:
            temp_f = celsius_to_fahrenheit(temperature)
        else:
            print("Invalid unit. Please enter 'F' or 'C'.")
            continue

        print()
        print(f"Wind Chill Results for {temp_f:.1f}°F:")
        for speed in range(5, 65, 5):
            chill = windchill(temp_f, speed)
            print(f"  At wind speed {speed:2} mph Windchill: {chill:.2f}°F")

        again = input("\nWould you like to calculate again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
