import csv
import datetime
import random

NUM_SALES = 100

def generate_sales_data_csv():
    """
    Generates a CSV file named "sales_data.csv" with sample sales data.

    Arguments: None

    Returns: None
    """
    data = [['SalesID', 'Date', 'Amount', 'EmployeeID']]
    start_date = '2023-01-01'
    end_date = '2023-12-31'
    num_sales = NUM_SALES

    for sales_id in range(1, num_sales + 1):
        date = random_date(start_date, end_date)
        amount = random.randint(1000, 10000)
        employee_id = random.randint(1, 10)
        data.append([sales_id, date, amount, employee_id])

    with open('sales_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Sales data CSV file generated successfully!")


def generate_employee_data_csv():
    """
    Generates a CSV file named "employee_data.csv" with sample employee data.

    Arguments: None

    Returns: None
    """
    data = [['EmployeeID', 'Name', 'Department', 'Salary']]
    num_employees = 10

    for employee_id in range(1, num_employees + 1):
        name = generate_random_name()
        department = generate_random_department()
        salary = random.randint(3000, 8000)
        data.append([employee_id, name, department, salary])

    with open('employee_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Employee data CSV file generated successfully!")


# Helper functions

def random_date(start_date, end_date):
    """
    Generates a random date between the given start and end dates.

    Arguments:
    - start_date (str): Start date in the format 'YYYY-MM-DD'.
    - end_date (str): End date in the format 'YYYY-MM-DD'.

    Returns:
    - random_date (str): Random date in the format 'YYYY-MM-DD'.
    """
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    random_days = (end_date - start_date).days
    random_date = start_date + datetime.timedelta(days=random.randint(0, random_days))
    return random_date.strftime("%Y-%m-%d")


def generate_random_name():
    """
    Generates a random name.

    Arguments: None

    Returns:
    - random_name (str): Random name.
    """
    first_names = ['John', 'Alice', 'Bob', 'Emma', 'Charlie', 'Olivia', 'Jacob', 'Sophia', 'Daniel', 'Mia']
    last_names = ['Smith', 'Johnson', 'Brown', 'Lee', 'Davis', 'Wilson', 'Clark', 'Hall', 'Baker', 'Garcia']
    random_name = random.choice(first_names) + ' ' + random.choice(last_names)
    return random_name


def generate_random_department():
    """
    Generates a random department.

    Arguments: None

    Returns:
    - random_department (str): Random department.
    """
    departments = ['Sales', 'Finance', 'Marketing', 'HR', 'IT', 'Operations', 'Research', 'Customer Service']
    random_department = random.choice(departments)
    return random_department


# Main program execution

if __name__ == '__main__':
    generate_sales_data_csv()
    generate_employee_data_csv()
