import csv

# -------- TestCase Class --------
class TestCase:
    def __init__(self, test_id, test_name, module):
        self.test_id = test_id
        self.test_name = test_name
        self.module = module
        self.status = "Not Executed"

    def execute_test(self, result):
        self.status = result

    def display_test_case(self):
        print(f"{self.test_id} | {self.test_name} | {self.module} | {self.status}")

    def to_csv_row(self):
        return [self.test_id, self.test_name, self.module, self.status, "NA"]


# -------- AutomatedTestCase Class --------
class AutomatedTestCase(TestCase):
    def __init__(self, test_id, test_name, module, automation_tool):
        super().__init__(test_id, test_name, module)
        self.automation_tool = automation_tool

    def display_test_case(self):
        print(f"{self.test_id} | {self.test_name} | {self.module} | {self.status} | {self.automation_tool}")

    def to_csv_row(self):
        return [self.test_id, self.test_name, self.module, self.status, self.automation_tool]


# -------- TestSuite Class --------
class TestSuite:
    def __init__(self, suite_name):
        self.suite_name = suite_name
        self.tests = []

    def add_test(self, test_case):
        self.tests.append(test_case)

    def run_all_tests(self):
        print(f"\nRunning Test Suite: {self.suite_name}")
        for test in self.tests:
            test.display_test_case()
            result = input("Enter result (Pass/Fail): ")
            test.execute_test(result)

    def save_results_to_csv(self, file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Test ID", "Test Name", "Module", "Status", "Automation Tool"])
            for test in self.tests:
                writer.writerow(test.to_csv_row())

    def summary_report(self):
        total = len(self.tests)
        passed = sum(1 for t in self.tests if t.status == "Pass")
        failed = sum(1 for t in self.tests if t.status == "Fail")
        not_executed = sum(1 for t in self.tests if t.status == "Not Executed")

        print("\n--- Test Execution Summary ---")
        print(f"Total Tests: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"Not Executed: {not_executed}")


# -------- Main Program --------
if __name__ == "__main__":
    tc1 = TestCase("TC001", "Login Test", "Auth")
    tc2 = TestCase("TC002", "Logout Test", "Auth")

    tc3 = AutomatedTestCase("TC003", "Create User", "User", "Selenium")
    tc4 = AutomatedTestCase("TC004", "Delete User", "User", "Playwright")

    suite = TestSuite("Regression Suite")

    suite.add_test(tc1)
    suite.add_test(tc2)
    suite.add_test(tc3)
    suite.add_test(tc4)

    suite.run_all_tests()
    suite.save_results_to_csv("test_results.csv")
    suite.summary_report()

