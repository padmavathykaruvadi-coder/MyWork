# 1) Define the BugTracker class
class BugTracker:
    def __init__(self):
        # 2) Initialize an empty dictionary to hold bug records
        self.bugs = {}

    # 3) Add a new bug (default status = "Open")
    def add_bug(self, bug_id, description, severity):
        self.bugs[bug_id] = {
            "description": description,
            "severity": severity,
            "status": "Open"
        }
        print(f"Bug {bug_id} added successfully.")

    # 4) Update the status of a bug
    def update_status(self, bug_id, new_status):
        if bug_id in self.bugs:
            self.bugs[bug_id]["status"] = new_status
            print(f"Bug {bug_id} status updated to {new_status}.")
        else:
            print(f"Bug {bug_id} not found.")

    # 5) List all bugs in a readable format
    def list_all_bugs(self):
        if not self.bugs:
            print("No bugs found.")
        else:
            print("\n--- All Bugs ---")
            for bug_id, details in self.bugs.items():
                print(f"Bug ID: {bug_id}")
                print(f"  Description: {details['description']}")
                print(f"  Severity: {details['severity']}")
                print(f"  Status: {details['status']}")
                print("-" * 30)


# 6) Main section to test functionality
if __name__ == "__main__":
    tracker = BugTracker()

    # 7) Add at least three bugs
    tracker.add_bug(101, "Login button not working", "High")
    tracker.add_bug(102, "UI misalignment on dashboard", "Medium")
    tracker.add_bug(103, "Slow response on search feature", "Low")

    # 8) Update statuses
    tracker.update_status(101, "In Progress")
    tracker.update_status(103, "Closed")

    # 9) Display all bugs
    tracker.list_all_bugs()
