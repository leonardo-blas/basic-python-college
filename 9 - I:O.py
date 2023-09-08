"""
Assignment #9, by Leonardo Blas.
06/19/2019
"""

import math

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

    def process_file(self, filename):
        return False

    def get_summary_statistics(self, active_sensors):
        if self._data_set is None:
            return None
        return (0, 0, 0)

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        if self._data_set is None:
            return None
        return 0

    def get_num_temps(self, active_sensors, lower_bound=None, upper_bound=None):
        """ To be implemented """
        if self._data_set is None:
            return None
        return 0

    def get_loaded_temps(self):
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
        if self._data_set:
            return len(self._data_set)
        return None

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
        name_input = input('Please provide a 3 to 20 character name for the dataset: ')
        try:
            current_set.name = name_input
            break
        except ValueError:
            print('Please enter between 3 and 20 characters.')
            continue

def choose_units():
    print('Choose Units Function Called')

def change_filter(sensor_list, active_sensors):
    """
    Print change filter menu and update active_sensors.
    :param sensor_list: list
    :param active_sensors: list
    :return: none
    """
    sensors = {  # Room Number: Sensor Number
        '4213': 0,
        '4201': 1,
        '4204': 2,
        '4218': 3,
        '4205': 4,
        'Out': 5
    }
    while True:
        print_filter(sensor_list, active_sensors)
        room_input = (input('\nType the sensor number to toggle (e.g.4201) or x to end '))
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
    if sorted_list_index <= 1:  # Escape case.
        return sorted_list
    for i in range(sorted_list_index):
        if sorted_list[i][key] > sorted_list[i + 1][key]:
            (sorted_list[i], sorted_list[i + 1]) = \
                (sorted_list[i + 1], sorted_list[i])
    # Recursive call.
    sorted_list = recursive_sort(sorted_list[:-1], key) + [sorted_list[-1]]
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
    sorted_sensors = recursive_sort(sensor_list, 0)  # Sort on Room Number string.
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
            new_file(current_set)
        elif integer_input == 2:
            choose_units()
        elif integer_input == 3:
            change_filter(sorted_sensors, active_sensors)
        elif integer_input == 4:
            print_summary_statistics(current_set, None)
        elif integer_input == 5:
            print_temp_by_day_time(current_set, None)
        elif integer_input == 6:
            print_histogram(current_set, None)
        elif integer_input == 7:
            print('Thank you for using the STEM Center Temperature Project')
            break

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
What is your choice? 1
Please enter the filename of the new dataset: Temperatures2017-08-06.csv
Loaded 11724 samples
Please provide a 3 to 20 character name for the dataset: My Data Set
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 1
Please enter the filename of the new dataset: Temperatures2017-08-06.csv
Loaded 11724 samples
Please provide a 3 to 20 character name for the dataset: no
Please enter between 3 and 20 characters.
Please provide a 3 to 20 character name for the dataset: okay
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 1
Please enter the filename of the new dataset: SpongebobSquarepants.csv
File not found. Program aborted.
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
Process finished with exit code 0
"""
