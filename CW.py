import pandas as pd
import numpy as np


execution_times = pd.Series([12, 15, 20, 18, 25, 30, 22])
print("Execution Times Series:")
print(execution_times)


middle_three = execution_times[2:5]
print("\nMiddle Three Execution Times:")
print(middle_three)


defects_array = np.array([10, 20, 23, 45, 50])
defects_series = pd.Series(defects_array)
print("\nDefects Series (from NumPy array):")
print(defects_series)

test_cases_dict = {
    "Senthil": 25,
    "Padma": 30,
    "Ben": 20,
    "Neeraj": 15,
    "Sarah": 18
}
test_cases_series = pd.Series(test_cases_dict)
print("\nTest Cases Executed by Engineers (Dictionary to Series):")
print(test_cases_series)
