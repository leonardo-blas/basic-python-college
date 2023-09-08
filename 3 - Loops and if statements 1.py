"""
Assignment #3, by Leonardo Blas
05/29/2019
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

def print_menu():
    """
    Print menu required by specs.
    :return: no return
    """
    print('\nMain Menu\n'
          '---------\n'
          '1 - Process a new data file\n'
          '2 - Choose units\n'
          '3 - Edit room filter\n'
          '4 - Show summary statistics\n'
          '5 - Show temperature by date and time\n'
          '6 - Show histogram of temperatures\n'
          '7 - Quit\n')

def new_file(dataset):
    print('New File Function Called')

def choose_units():
    print('Choose Units Function Called')

def change_filter(sensor_list, active_sensors):
    print('Change Filter Function Called')

def print_summary_statistics(dataset, active_sensors):
    print('Summary Statistics Function Called')

def print_temp_by_day_time(dataset, active_sensors):
    print('Print Temp by Day/Time Function Called')

def print_histogram(dataset, active_sensors):
    print('Print Histogram Function Called')

def main():
    print_header()
    while True:
        print_menu()
        try:
            integer_input = int(input('What is your choice? '))
        except ValueError:
            print('*** Please enter a number only ***')
            continue
        if 1 <= integer_input <= 7:
            if integer_input == 1:
                new_file(None)
            elif integer_input == 2:
                choose_units()
            elif integer_input == 3:
                change_filter(None, None)
            elif integer_input == 4:
                print_summary_statistics(None, None)
            elif integer_input == 5:
                print_temp_by_day_time(None, None)
            elif integer_input == 6:
                print_histogram(None, None)
            elif integer_input == 7:
                print('Thank you for using the STEM Center Temperature Project')
                break
        else:
            print('Invalid Choice')

if __name__ == "__main__":
    main()


"""
STEM Center Temperature Project
Leonardo Blas
Main Menu
---------
1. - Process a new data file
2. - Choose units
3. - Edit room filter
4. - Show summary statistics
5. - Show temperature by date and time
6. - Show histogram of temperatures
7. - Quit
What is your choice? 1
New File Function Called
Main Menu
---------
1. - Process a new data file
2. - Choose units
3. - Edit room filter
4. - Show summary statistics
5. - Show temperature by date and time
6. - Show histogram of temperatures
7. - Quit
What is your choice? 2
Choose Units Function Called
Main Menu
---------
1. - Process a new data file
2. - Choose units
3. - Edit room filter
4. - Show summary statistics
5. - Show temperature by date and time
6. - Show histogram of temperatures
7. - Quit
What is your choice? 3
Change Filter Function Called
Main Menu
---------
1. - Process a new data file
2. - Choose units
3. - Edit room filter
4. - Show summary statistics
5. - Show temperature by date and time
6. - Show histogram of temperatures
7. - Quit
What is your choice? 4
Summary Statistics Function Called
Main Menu
---------
1. - Process a new data file
2. - Choose units
3. - Edit room filter
4. - Show summary statistics
5. - Show temperature by date and time
6. - Show histogram of temperatures
7. - Quit
What is your choice? 5
Print Temp by Day/Time Function Called
Main Menu
---------
1. - Process a new data file
2. - Choose units
3. - Edit room filter
4. - Show summary statistics
5. - Show temperature by date and time
6. - Show histogram of temperatures
7. - Quit
What is your choice? 6
Print Histogram Function Called
Main Menu
---------
1. - Process a new data file
2. - Choose units
3. - Edit room filter
4. - Show summary statistics
5. - Show temperature by date and time
6. - Show histogram of temperatures
7. - Quit
What is your choice? -99
Invalid Choice
Main Menu
---------
1. - Process a new data file
2. - Choose units
3. - Edit room filter
4. - Show summary statistics
5. - Show temperature by date and time
6. - Show histogram of temperatures
7. - Quit
What is your choice? 11
Invalid Choice
Main Menu
---------
1. - Process a new data file
2. - Choose units
3. - Edit room filter
4. - Show summary statistics
5. - Show temperature by date and time
6. - Show histogram of temperatures
7. - Quit
What is your choice? t
*** Please print a number only ***
Invalid Choice
Main Menu
---------
1. - Process a new data file
2. - Choose units
3. - Edit room filter
4. - Show summary statistics
5. - Show temperature by date and time
6. - Show histogram of temperatures
7. - Quit
What is your choice? wawa
*** Please print a number only ***
Invalid Choice
Main Menu
---------
1. - Process a new data file
2. - Choose units
3. - Edit room filter
4. - Show summary statistics
5. - Show temperature by date and time
6. - Show histogram of temperatures
7. - Quit
What is your choice? 282823
Invalid Choice
Main Menu
---------
1. - Process a new data file
2. - Choose units
3. - Edit room filter
4. - Show summary statistics
5. - Show temperature by date and time
6. - Show histogram of temperatures
7. - Quit
What is your choice? 7
Thank you for using the STEM Center Temperature Project
Process finished with exit code 0
"""
