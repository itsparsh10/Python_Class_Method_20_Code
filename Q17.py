# Develop a time tracking system for employees with classes for employees,
# projects, and time entries. Implement methods for logging hours, generating
# timesheets, and calculating overtime.
import datetime

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.projects = []

    def log_hours(self, project, hours, date):
        time_entry = TimeEntry(self, project, hours, date)
        project.add_time_entry(time_entry)

    def generate_timesheet(self, start_date, end_date):
        timesheet = {}
        for project in self.projects:
            timesheet[project.name] = project.get_hours_worked(self.employee_id, start_date, end_date)
        return timesheet

    def calculate_overtime(self, start_date, end_date):
        total_hours = sum(self.generate_timesheet(start_date, end_date).values())
        if total_hours > 40:
            return total_hours - 40
        else:
            return 0

class Project:
    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name
        self.time_entries = []

    def add_time_entry(self, time_entry):
        self.time_entries.append(time_entry)

    def get_hours_worked(self, employee_id, start_date, end_date):
        hours_worked = 0
        for entry in self.time_entries:
            if entry.employee.employee_id == employee_id and start_date <= entry.date <= end_date:
                hours_worked += entry.hours
        return hours_worked

class TimeEntry:
    def __init__(self, employee, project, hours, date):
        self.employee = employee
        self.project = project
        self.hours = hours
        self.date = date

def main():
    employee1 = Employee(1, "Alice")
    employee2 = Employee(2, "Bob")

    project1 = Project(101, "Project A")
    project2 = Project(102, "Project B")

    employee1.projects.extend([project1, project2])
    employee2.projects.extend([project1, project2])

    # Log hours for employees
    employee1.log_hours(project1, 20, datetime.date(2023, 1, 1))
    employee1.log_hours(project2, 21, datetime.date(2023, 1, 2))
    employee2.log_hours(project1, 7, datetime.date(2023, 1, 1))
    employee2.log_hours(project2, 6, datetime.date(2023, 1, 2))

    # Generate timesheet for employees
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 1, 2)

    timesheet_employee1 = employee1.generate_timesheet(start_date, end_date)
    timesheet_employee2 = employee2.generate_timesheet(start_date, end_date)

    print("Timesheet for Employee 1:")
    print(timesheet_employee1)

    print("\nTimesheet for Employee 2:")
    print(timesheet_employee2)

    # Calculate overtime for employees
    overtime_employee1 = employee1.calculate_overtime(start_date, end_date)
    overtime_employee2 = employee2.calculate_overtime(start_date, end_date)

    print("\nOvertime for Employee 1:", overtime_employee1, "hours")
    print("Overtime for Employee 2:", overtime_employee2, "hours")

if __name__ == "__main__":
    main()