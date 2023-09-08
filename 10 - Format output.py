"""
Assignment #10, by Leonardo Blas.
06/23/2019
"""

import math

UNITS = {0: ("Celsius", "C"), 1: ("Fahrenheit", "F"), 2: ("Kelvin", "K")}
current_unit = 0

class TempDataset:
    number_of_dataset_objects = 0
    MINLENGTH = 3
    MAXLENGTH = 20

    def __init__(self):
        """ initialize instance variables """
        self._data_set = None
        self._name = "Unnamed"
        TempDataset.number_of_dataset_objects += 1

    @property
    def name(self):
        """ takes no arguments, returns the name of our data """
        return self._name

    @name.setter
    def name(self, new_name):
        """ accepts and stores a string representing a name for our data
        returns FALSE if string is too short or too long
        """
        if (len(new_name) < TempDataset.MINLENGTH or len(new_name) > TempDataset.MAXLENGTH):
            raise ValueError
        self._name = new_name

    def get_num_temps(self, active_sensors, lower_bound=None, upper_bound=None):
        """ To be implemented """
        if self._data_set is None:
            return None
        return 0

    def process_file(self, filename):
        """
        Method for opening and processing files.
        :param filename: str, name of file to be processed.
        :return: bool
        """
        self._data_set = []
        try:
            my_file = open(filename)
            for next_line in my_file:
                next_line = next_line.split(',')
                if next_line[3] == 'TEMP':
                    day = int(next_line[0])
                    time = math.floor(24 * float(next_line[1]))
                    sensor = int(next_line[2])
                    temp = float(next_line[4])
                    data_tuple = (day, time, sensor, temp)
                    self._data_set.append(data_tuple)
            my_file.close()
            return True
        except FileNotFoundError:
            print("File not found. Program aborted.")
            return False

    def get_loaded_temps(self):
        """
        Return None or number of loaded samples.
        :return: None or int.
        """
        if self._data_set is None:
            return None
        return int(len(self._data_set))

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        """
        Return temperature average during a particular time and day.
        :param active_sensors: list
        :param day: int
        :param time: float
        :return: float or None
        """
        if not self._data_set or self._data_set is None or not active_sensors:
            return None
        temp_data = [i[3] for i in self._data_set if
                     day == i[0] and time == i[1] and i[2] in active_sensors]
        if not temp_data:
            return None
        temp_data_sum = 0
        for i in temp_data:
            temp_data_sum += i
        return temp_data_sum / len(temp_data)

    def get_summary_statistics(self, active_sensors):
        """
        Process list and returns temperature tuple.
        :param active_sensors: list
        :return: tuple
        """
        if self._data_set is None or active_sensors is None:
            return None
        temp_data = [i[3] for i in self._data_set if i[2] in active_sensors]
        if not temp_data:
            return None
        temp_data_min = min(temp_data)
        temp_data_max = max(temp_data)
        temp_data_avg = sum(temp_data) / len(temp_data)
        return temp_data_min, temp_data_max, temp_data_avg

    @classmethod
    def get_num_objects(cls):
        """ Takes no arguments,
        Returns the number of objects that have been created
        """
        return cls.number_of_dataset_objects

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
        fahrenheit_value = ((celsius_value * (9 / 5)) + 32)
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

def new_file(current_set):
    """
    Ask for a file name and load the data.
    :param current_set:
    :return:
    """
    filename_input = input('Please enter the filename of the new dataset: ')
    if not current_set.process_file(filename_input):
        return
    print(f'Loaded {current_set.get_loaded_temps()} samples')
    while True:
        name_input = input(
            'Please provide a 3 to 20 character name for the dataset: ')
        try:
            current_set.name = name_input
            break
        except ValueError:
            print('Please enter between 3 and 20 characters.')
            continue

def choose_units():
    """
    Take user units election, check it, and assign it.
    :return: no return
    """
    global current_unit
    print(f'Current units in {UNITS[current_unit][0]}')
    while True:
        try:
            print('Choose new units: ')
            print('0 - Celsius\n'
                  '1 - Fahrenheit\n'
                  '2 - Kelvin')
            input_unit = int(input('Which unit?\n'))
            if input_unit not in UNITS.keys():
                print('Please choose a unit from the list.')
            else:
                current_unit = input_unit
                break
        except ValueError:
            print('*** Please print a number only ***')

def change_filter(sensor_list, active_sensors):
    """
    Print change filter menu and update active_sensors.
    :param sensor_list: list
    :param active_sensors: list
    :return: none
    """
    sensors = {  # Room Number: Sensor Number
        '4213': 0, '4201': 1, '4204': 2, '4218': 3, '4205': 4, 'Out': 5}
    while True:
        print_filter(sensor_list, active_sensors)
        room_input = (
            input('\nType the sensor number to toggle (e.g.4201) or x to end '))
        if room_input == 'x':
            break
        # Checking with dictionary, as requested.
        if room_input not in sensors.keys():
            print('Invalid Sensor')
        # Checking with dictionary, as requested.
        if room_input in sensors.keys():
            for i in range(len(sensor_list)):
                if sensor_list[i][0] == room_input:
                    if sensor_list[i][2] in active_sensors:
                        active_sensors.remove(sensor_list[i][2])
                    break
            if sensor_list[i][2] not in active_sensors:
                active_sensors.append(sensor_list[i][2])
                break

def print_summary_statistics(dataset, active_sensors):
    """
    Helper function for get_summary_statistics. Prints a menu.
    :param dataset: TempDataSet
    :param active_sensors:
    :return: no return
    """
    if dataset.get_summary_statistics(active_sensors) is None:
        print('Please load data file and make sure at least one '
              'sensor is active.')
        return
    print(f'Summary statistics for {dataset.name}')
    summary_tuple = dataset.get_summary_statistics(active_sensors)
    min_data = convert_units(summary_tuple[0], current_unit)
    max_data = convert_units(summary_tuple[1], current_unit)
    avg_data = convert_units(summary_tuple[2], current_unit)
    min_data_format = format(min_data, '.2f')
    max_data_format = format(max_data, '.2f')
    avg_data_format = format(avg_data, '.2f')
    print(f'Minimum Temperature: {min_data_format} {UNITS[current_unit][1]}')
    print(f'Maximum Temperature: {max_data_format} {UNITS[current_unit][1]}')
    print(f'Average Temperature: {avg_data_format} {UNITS[current_unit][1]}')

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
    if sorted_list_index <= 1:  # Escape case.
        return sorted_list
    for i in range(sorted_list_index):
        if sorted_list[i][key] > sorted_list[i + 1][key]:
            (sorted_list[i], sorted_list[i + 1]) = (
                sorted_list[i + 1], sorted_list[i])
    # Recursive call.
    sorted_list = recursive_sort(sorted_list[:-1], key) + [
        sorted_list[-1]]
    return sorted_list

def print_filter(sensor_list, active_sensors):
    """
    Print [ACTIVE] next to active sensors, nothing next to inactive ones.
    :param sensor_list: list
    :param active_sensors: list
    :return: none
    """
    print('')
    for i in range(len(sensor_list)):
        if sensor_list[i][2] in active_sensors:
            print(f'{sensor_list[i][0]}: {sensor_list[i][1]} [ACTIVE]')
        else:
            print(f'{sensor_list[i][0]}: {sensor_list[i][1]}')

def main():
    current_set = TempDataset()
    sensor_list = [  # (Room Number, Room Description, Sensor Number).
        ('4213', 'STEM Center', 0),
        ('4201', 'Foundations Lab', 1),
        ('4204', 'CS Lab', 2),
        ('4218', 'Workshop Room', 3),
        ('4205', 'Tiled Room', 4),
        ('Out', 'Outside', 5)
    ]  # Not generating Sensor Numbers because pattern is not mandatory.
    active_sensors = [i[2] for i in sensor_list]
    # Sort on Room Number string.
    sorted_sensors = recursive_sort(sensor_list, 0)
    print_header()
    while True:
        print_menu()
        # 5 = Friday, 7 = (7AM - 8AM)
        print(current_set.get_avg_temperature_day_time(active_sensors, 5, 7))
        integer_input = (input('What is your choice? '))
        try:
            choice = int(integer_input)
            if 1 > choice or choice > 7:
                print('Invalid Choice')
            elif choice == 1:
                new_file(current_set)
            elif choice == 2:
                choose_units()
            elif choice == 3:
                change_filter(sorted_sensors, active_sensors)
            elif choice == 4:
                print_summary_statistics(current_set, active_sensors)
            elif choice == 5:
                print_temp_by_day_time(current_set, None)
            elif choice == 6:
                print_histogram(current_set, None)
            elif choice == 7:
                print('Thank you for using the STEM Center Temperature Project')
                break
        except ValueError:
            print('*** Please print a number only ***')

if __name__ == "__main__":
    main()


"""
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
None
What is your choice? 4
Please load data file and make sure at least one sensor is active.
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
None
What is your choice? 1
Please enter the filename of the new dataset: Temperatures2017-08-06.csv
Loaded 11724 samples
Please provide a 3 to 20 character name for the dataset: no
Please enter between 3 and 20 characters.
Please provide a 3 to 20 character name for the dataset: Spongy
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
20.45544117647059
What is your choice? 4
Summary statistics for Spongy
Minimum Temperature: 16.55 C
Maximum Temperature: 28.42 C
Average Temperature: 21.47 C
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
20.45544117647059
What is your choice? 2
Current units in Celsius
Choose new units:
0 - Celsius
1 - Fahrenheit
2 - Kelvin
Which unit?
5
Please choose a unit from the list.
Choose new units:
0 - Celsius
1 - Fahrenheit
2 - Kelvin
Which unit?
-1
Please choose a unit from the list.
Choose new units:
0 - Celsius
1 - Fahrenheit
2 - Kelvin
Which unit?
g
*** Please print a number only ***
Choose new units:
0 - Celsius
1 - Fahrenheit
2 - Kelvin
Which unit?
tut
*** Please print a number only ***
Choose new units:
0 - Celsius
1 - Fahrenheit
2 - Kelvin
Which unit?
2
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
20.45544117647059
What is your choice? 3
4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor number to toggle (e.g.4201) or x to end 4218
4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room
Out: Outside [ACTIVE]
Type the sensor number to toggle (e.g.4201) or x to end x
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
20.276250000000005
What is your choice? 4
Summary statistics for Spongy
Minimum Temperature: 289.70 K
Maximum Temperature: 301.57 K
Average Temperature: 294.65 K
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
20.276250000000005
What is your choice? 3
4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room
Out: Outside [ACTIVE]
Type the sensor number to toggle (e.g.4201) or x to end 4201
4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room
Out: Outside [ACTIVE]
Type the sensor number to toggle (e.g.4201) or x to end 4204
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room
Out: Outside [ACTIVE]
Type the sensor number to toggle (e.g.4201) or x to end 4205
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room
Out: Outside [ACTIVE]
Type the sensor number to toggle (e.g.4201) or x to end 4213
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room
Out: Outside [ACTIVE]
Type the sensor number to toggle (e.g.4201) or x to end Out
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room
Out: Outside
Type the sensor number to toggle (e.g.4201) or x to end x
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
None
What is your choice? 4
Please load data file and make sure at least one sensor is active.
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
None
What is your choice? 3
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room
Out: Outside
Type the sensor number to toggle (e.g.4201) or x to end Out
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room
Out: Outside [ACTIVE]
Type the sensor number to toggle (e.g.4201) or x to end 4
Invalid Sensor
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room
Out: Outside [ACTIVE]
Type the sensor number to toggle (e.g.4201) or x to end x
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
18.549166666666668
What is your choice? 4
Summary statistics for Spongy
Minimum Temperature: 289.70 K
Maximum Temperature: 301.57 K
Average Temperature: 295.16 K
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
18.549166666666668
What is your choice? 7
Thank you for using the STEM Center Temperature Project
Process finished with exit code 0
"""
