import numpy as np

class TestReport:
    def __init__(self, execution_times):
        self.execution_times = execution_times
    def average_time(self):
        return np.mean(self.execution_times)
    def max_time(self):
        return np.max(self.execution_times)

class RegressionReport(TestReport):
    def slow_tests(self, threshold):
        return self.execution_times[self.execution_times > threshold]

times = np.array([12, 18, 25, 30, 5, 40, 22, 15, 35, 10])
r = RegressionReport(times)
print(r.average_time())
print(r.max_time())
print(r.slow_tests(20))