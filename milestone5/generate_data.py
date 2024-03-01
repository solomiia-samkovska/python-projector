from faker import Faker
import csv

def generate_employee():

    fake = Faker()

    fname = fake.name()
    fhiring = fake.date_between(start_date = '-15y', end_date = 'today')
    fdepartment = fake.random_element(elements = ('Engineering', 'Marketing', 'Sales', 'HR', 'Finance', 'R&D', 'IT'))
    fdob = fake.date_of_birth(minimum_age = 18, maximum_age = 65)
    employee = {'Name': fname, 'Hiring date': fhiring, 'Department': fdepartment, 'Birthday': fdob}
    
    return employee


def generateDB(quantity):
    
    with open('database.csv', 'w', newline='') as file:
        fieldnames = ['Name', 'Hiring date', 'Department', 'Birthday']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in range(quantity):
            row = generate_employee()               
            writer.writerow(row)


generateDB(50)
