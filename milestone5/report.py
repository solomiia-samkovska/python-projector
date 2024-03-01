import csv
import sys
from datetime import datetime


def load_employees(file_name):
    employees = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row)
        return employees


def events_report(list_empl, month, event: str):

    event_department_dict = {}

    for employee in list_empl:

        event_date = datetime.strptime(employee[event], '%Y-%m-%d')
        event_month = event_date.strftime('%B')

        if event_month == month:
            department = employee['Department']
            name = employee['Name']
            if department in event_department_dict:
                event_department_dict[department].append(name)
            else:
                event_department_dict[department] = [name]

    return event_department_dict


def report_printing(month):

    total_bd = total_calc(bd_dict)
    total_annivers = total_calc(annivers_dict)

    print(f"Report for {month} generated")
    print()
    print("--- Birthdays ---")
    print(f"Total:{total_bd}") 
    if total_bd != 0:
        department_statistic(bd_dict)

    print()
    print("--- Anniversaries ---")
    print(f"Total:{total_annivers}")    
    if total_annivers != 0:
        department_statistic(annivers_dict)


def total_calc(dep_employee_dict):
    total = 0
    for list_names in dep_employee_dict.values():
        total +=len(list_names)
    return total


def department_statistic(dep_employee_dict):
    print("By department:")
    for department, list_names in dep_employee_dict.items():
        print(f"- {department}: {len(list_names)}")
        if sys.argv[-1] == '-v':
            for name in list_names:
                print(name)


file = sys.argv[1]
month = sys.argv[2].capitalize()


list_employees = load_employees(file)
bd_dict = events_report(list_employees, month, "Birthday")
annivers_dict = events_report(list_employees, month, "Hiring date")
report_printing(month)
