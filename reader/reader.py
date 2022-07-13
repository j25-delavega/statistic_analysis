def reader(file_name):

    data = []

    # Using readline()
    file = open(file_name, 'r')
    count = 0

    while True:
        count += 1

        # Get next line from file
        line = file.readline()
        if len(line):
            data.append(line)
        # if line is empty
        # end of file is reached
        if not line:
            break
        # print("Line{}: {}".format(count, line.strip()))

    file.close()
    return data
