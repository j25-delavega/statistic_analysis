from reader.reader import reader
from printer.data_printer import data_printer

if __name__ == '__main__':

    path = "file_for_reading/"
    file_name = path + "data.dat"

    data = reader(file_name)
    data_printer(data)

