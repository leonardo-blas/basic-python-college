"""
Assignment #2, by Leonardo Blas
05/24/2019
"""

def print_header():
    """Print required sentences."""
    print("STEM Center Temperature Project")
    print("Leonardo Blas")

def convert_units(celsius_value, units):
    """
    Convert celsius input into other temperature scales.

    :param celsius_value: float
    :param units: int
    :return: float
    """
    if units == 0:
        return celsius_value
    if units == 1:
        fahrenheit_value = ((celsius_value * (9/5)) + 32)
        return fahrenheit_value
    if units == 2:
        kelvin_value = celsius_value + 273.15
        return kelvin_value

def main():
    print_header()
    celsius_input = input("Please enter a temperature in degrees Celsius:")
    fahrenheit_conversion = convert_units(float(celsius_input), 1)
    kelvin_conversion = convert_units(float(celsius_input), 2)
    print(f"That's {fahrenheit_conversion} Fahrenheit and {kelvin_conversion} Kelvin.")

if __name__ == "__main__":
    main()


"""
STEM Center Temperature Project
Leonardo Blas
Please enter a temperature in degrees Celsius:45
That's 113.0 and 318.15 Kelvin.
Process finished with exit code 0
"""
