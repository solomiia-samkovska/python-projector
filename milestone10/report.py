import csv
import sys
from datetime import datetime


def get_BD_report(request_month, request_department):

    employees = load_employees('database.csv')
    reportByMonth = events_report(employees, request_month, 'Birthday')
    if request_department in reportByMonth:
        report = reportByMonth[request_department]
    else:
        report = {}

    total = len(report)
    employee_list = []

    for employee in report:
        employee['Birthday'] = datetime.strptime(employee['Birthday'] , "%Y-%m-%d").strftime("%b %d")
        employee = {'id': employee['ID'], 'name': employee['Name'], 'birthday': employee['Birthday']}
        employee_list.append(employee)

    response = {'total': total, 'employees': employee_list}

    return response


def get_annivers_report(request_month, request_department):

    employees = load_employees('database.csv')
    reportByMonth = events_report(employees, request_month, 'Hiring date')
    if request_department in reportByMonth:
        report = reportByMonth[request_department]
    else:
        report = {}

    total = len(report)
    employee_list = []

    for employee in report:
        employee['Hiring date'] = datetime.strptime(employee['Hiring date'] , "%Y-%m-%d").strftime("%b %d")
        employee = {'id': employee['ID'], 'name': employee['Name'], 'birthday': employee['Hiring date']}
        employee_list.append(employee)

    response = {'total': total, 'employees': employee_list}

    return response


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

        if event_month == month.capitalize():
            department = employee['Department']

            if department in event_department_dict:
                event_department_dict[department].append(employee)
            else:
                event_department_dict[department] = [employee]
        
    return event_department_dict