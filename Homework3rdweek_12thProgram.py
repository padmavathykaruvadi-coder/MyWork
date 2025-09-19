import numpy as np

class ManualTester:
    def analyze(self, data):
        print(data[:5])

class AutomationTester:
    def analyze(self, data):
        print(data.min())

class PerformanceTester:
    def analyze(self, data):
        print(np.percentile(data, 95))

def show_analysis(tester, data):
    tester.analyze(data)

data = np.array([12, 18, 25, 30, 5, 40, 22, 15, 35, 10, 28, 33])
for t in (ManualTester(), AutomationTester(), PerformanceTester()):
    show_analysis(t, data)
