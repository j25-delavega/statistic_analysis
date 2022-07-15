class DataClass(object):
    def __init__(self, file_name):
        self.number_of_points = 0  # the depot is not included
        self.number_of_metrics = 0
        self.worst_values = []
        self.best_values = []
        self.seed_values = []
        self.routes = []
        self.metric_values = []
        self.file_name = file_name

    def get_route(self, first_list):
        route = []
        for i in range(1, self.number_of_points + 2):
            route.append(int(first_list[i]))
        return route

    def get_metrics(self, line_list):
        metrics = []
        for i in range(self.number_of_points + 2, self.number_of_points + self.number_of_metrics + 2):
            metrics.append(float(line_list[i]))
        return metrics

    def update_best_and_worst_values(self):
        for i in range(0, self.number_of_metrics):
            if self.metric_values[len(self.metric_values) - 1][i] < self.best_values[i]:
                self.best_values[i] = self.metric_values[len(self.metric_values) - 1][i]
            if self.metric_values[len(self.metric_values) - 1][i] > self.worst_values[i]:
                self.worst_values[i] = self.metric_values[len(self.metric_values) - 1][i]

    def reader(self):
        file = open(self.file_name, 'r')
        count = 0

        while True:
            count += 1
            # Get next line from file
            line = file.readline()
            if len(line):
                split_line = line.split()
                if count == 1:
                    self.number_of_points = int(split_line[0])
                    self.number_of_metrics = int(split_line[1])
                    self.worst_values = [float('-inf')] * self.number_of_metrics
                    self.best_values = [float('inf')] * self.number_of_metrics
                else:
                    self.seed_values.append(int(split_line[0]))
                    self.routes.append(self.get_route(split_line))
                    self.metric_values.append(self.get_metrics(split_line))
                    self.update_best_and_worst_values()

            if not line:
                break

        file.close()

    def get_data_to_analyze(self):
        data = []
        for j in range(0, self.number_of_metrics):
            values = []
            for i in range(0, len(self.metric_values)):
                value = abs(self.metric_values[i][j] - self.best_values[j]) / abs(
                    self.worst_values[j] - self.best_values[j])
                values.append(value)
            data.append(values)

        return data
