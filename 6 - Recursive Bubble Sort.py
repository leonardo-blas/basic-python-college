"""
Assignment #6, by Leonardo Blas.
06/09/2019
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

def recursive_sort(list_to_sort, key=0):
    """
    Required recursive Bubble Sort.
    
    :param list_to_sort: list of tuples
    :param key: 0 or 1, to sort by tuples' first or second value
    :return: list of tuples (sorted)
    """
    sorted_list = list_to_sort[:]
    sorted_list_index = len(sorted_list) - 1
    if sorted_list_index == 1:  # Escape case.
        return sorted_list
    for i in range(sorted_list_index):
        if sorted_list[i][key] > sorted_list[i + 1][key]:
            (sorted_list[i], sorted_list[i + 1]) = (sorted_list[i + 1], sorted_list[i])
    # Recursive call.
    sorted_list = recursive_sort(sorted_list[:-1], key) + [sorted_list[-1]]
    return sorted_list

def main():
    sensor_list = [  # (Room Number, Room Description, Sensor Number).
        ('4213', 'STEM Center', 0),
        ('4201', 'Foundations Lab', 1),
        ('4204', 'CS Lab', 2),
        ('4218', 'Workshop Room', 3),
        ('4205', 'Tiled Room', 4),
        ('Out', 'Outside', 5)
    ]  # Not generating Sensor Numbers because the pattern is not mandatory.
    active_sensors = [i[2] for i in sensor_list]  # Will modify later.
    print(sensor_list)
    print(recursive_sort(sensor_list, 0))
    print(recursive_sort(sensor_list, 1))
    print(sensor_list)
    print_header()
    while True:
        print_menu()
        try:
            integer_input = int(input('What is your choice? '))
        except ValueError:
            print('*** Please print a number only ***')
        if 1 > integer_input or integer_input > 7:
            print('Invalid Choice')
        elif integer_input == 1:
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

if __name__ == "__main__":
    main()


"""
[('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]
[('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4205', 'Tiled Room', 4), ('4213', 'STEM Center', 0), ('4218', 'Workshop Room', 3), ('Out', 'Outside', 5)]
[('4204', 'CS Lab', 2), ('4201', 'Foundations Lab', 1), ('Out', 'Outside', 5), ('4213', 'STEM Center', 0), ('4205', 'Tiled Room', 4), ('4218', 'Workshop Room', 3)]
[('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]
STEM Center Temperature Project
Leonardo Blas

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 7
Thank you for using the STEM Center Temperature Project
"""
