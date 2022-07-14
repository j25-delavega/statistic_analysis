from reader.reader import DataClass
from printer.data_printer import data_printer

if __name__ == '__main__':

    path = "file_for_reading/"
    file_name = path + "data.dat"

    reader = DataClass(file_name)
    reader.reader()
    data = reader.get_data_to_analyze()
    data_printer(data)

