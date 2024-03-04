import requests
import sys

def get_birtdays_info(month, department):

    url = f'http://localhost:5000/birthdays?month={month}&department={department}'
    response = requests.get(url)

    return response


month = sys.argv[1]
department = sys.argv[2]

response = get_birtdays_info(month, department)

print(f'Report for {department} department for {month.capitalize()} fetched.')
print(f'Total: {response.json()["total"]}')
print('Employees:')
for employee in response.json()["employees"]:
    print(f'- {employee["birthday"]}, {employee["name"]}')

