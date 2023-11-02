import csv
import matplotlib.pyplot as plt
import os


def read_sales_data():
    """
    Reads the sales data from the "sales_data.csv" file.

    Arguments: None

    Returns:
    - sales_data (list): List of dictionaries representing sales data.
    """
    sales_data_tuple:tuple = []
    sales_data: list = []
    current_row: tuple = []
    full_path = os.path.dirname(os.path.realpath(__file__))
    full_path = f"{full_path}/sales_data.csv"
    print(full_path)

    with open(full_path, "r") as file_sales:
        reader = csv.reader(file_sales)
        next(reader)
        sales_data_tuple = [tuple(row) for row in reader]
        for i in range(len(sales_data_tuple)):
            current_row = sales_data_tuple[i]
            sales_data.append({current_row[0]: sales_data_tuple[i]})
    return sales_data
         


def read_employee_data():
    """
    Reads the employee data from the "employee_data.csv" file.

    Arguments: None

    Returns:
    - employee_data (list): List of dictionaries representing employee data.
    """
    employee_data_tuple:tuple = []
    employee_data: list = []
    current_row: tuple = []
    full_path = os.path.dirname(os.path.realpath(__file__))
    full_path = f"{full_path}/employee_data.csv"
    print(full_path)

    with open(full_path, "r") as file_sales:
        reader = csv.reader(file_sales)
        next(reader)
        employee_data_tuple = [tuple(row) for row in reader]
        for i in range(len(employee_data_tuple)):
            current_row = employee_data_tuple[i]
            employee_data.append({current_row[0]: employee_data_tuple[i]})
    return employee_data


def calculate_total_sales(sales_data):
    """
    Calculates the total sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - total_sales (float): Total sales amount.
    """
    s = 0
    for sale in sales_data:
        s += float((list(sale.values())[0])[2])
    return s
        
    


def calculate_average_sales(sales_data):
    """
    Calculates the average sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - average_sales (float): Average sales amount.
    """
    return calculate_total_sales(sales_data) / len(sales_data)

def calculate_median_sales(sales_data):
    """
    Calculates the median sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - median_sales (float): Median sales amount.
    """
    list_sales = sorted([float((list(sale.values())[0])[2]) for sale in sales_data])
    l = len(list_sales)
    mid = l//2
    return list_sales[mid] if mid %2 == 1 else (list_sales[mid-1] + list_sales[mid])/2


def calculate_total_salary_expenses(employee_data):
    """
    Calculates the total salary expenses.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - total_salary_expenses (float): Total salary expenses.
    """
    return sum([float((list(employee.values())[0])[3]) for employee in employee_data])
        


def calculate_average_salary(employee_data):
    """
    Calculates the average salary.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - average_salary (float): Average salary.
    """
    return calculate_total_salary_expenses(employee_data) / len(employee_data)

def calculate_median_salary(employee_data):
    """
    Calculates the median salary.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - median_salary (float): Median salary.
    """
    list_salary = [float((list(employee.values())[0])[3]) for employee in employee_data]
    l = len(list_salary)
    mid = l//2
    return list_salary[mid] if mid%2 == 1 else (list_salary[mid-1] + list_salary[mid])/2


def find_employee_with_highest_sales(sales_data, employee_data):
    """
    Finds the employee with the highest sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - employee_name (str): Name of the employee with the highest sales amount.
    - department_name (str): Name of the department of the employee with the highest sales amount.
    """
    se = {}
    for sale in sales_data:
        sale_tuple = list(sale.values())[0]
        if sale_tuple[3] in se:
            se[sale_tuple[3]] += int(sale_tuple[2])
        else:
            se[sale_tuple[3]] = int(sale_tuple[2])

    ma = (0,0)
    for k, v in se.items():
      if ma[1] < v:
          ma = (k, v)

    employee = (list(employee_data[int(ma[0])].values())[0])
    return employee[1], employee[2]


# def plot_sales_by_department(sales_data, employee_data):
#     """
#     Plots a bar chart showing the total sales by department.

#     Arguments:
#     - sales_data (list): List of dictionaries representing sales data.
#     - employee_data (list): List of dictionaries representing employee data.

#     Returns: None
#     """
#     pass


# def plot_sales_vs_salary(sales_data, employee_data):
#     """
#     Plots a scatter plot showing the relationship between sales and salary.

#     Arguments:
#     - sales_data (list): List of dictionaries representing sales data.
#     - employee_data (list): List of dictionaries representing employee data.

#     Returns: None
#     """
#     pass


def main():
    # Read sales data
    sales_data = read_sales_data()
    # print(sales_data)

    # Read employee data
    employee_data = read_employee_data()
    # print(employee_data)

    # Calculate total sales amount
    total_sales = calculate_total_sales(sales_data)
    print("Total Sales Amount:", total_sales)

    # Calculate average sales amount
    average_sales = calculate_average_sales(sales_data)
    print("Average Sales Amount:", average_sales)

    # Calculate median sales amount
    median_sales = calculate_median_sales(sales_data)
    print("Median Sales Amount:", median_sales)

    # Calculate total salary expenses
    total_salary_expenses = calculate_total_salary_expenses(employee_data)
    print("Total Salary Expenses:", total_salary_expenses)

    # Calculate average salary
    average_salary = calculate_average_salary(employee_data)
    print("Average Salary:", average_salary)

    # Calculate median salary
    median_salary = calculate_median_salary(employee_data)
    print("Median Salary:", median_salary)

    # Find the employee with the highest sales amount
    highest_sales_employee, highest_sales_employee_dep = find_employee_with_highest_sales(sales_data, employee_data)
    print("Employee with Highest Sales Amount:", highest_sales_employee, highest_sales_employee_dep)

    # Find the department with the highest sales
    highest_sales_department = highest_sales_employee_dep
    print("Department with Highest Sales:", highest_sales_department)

    # Plot total sales by department
    # plot_sales_by_department(sales_data, employee_data)

    # Plot sales vs. salary
    # plot_sales_vs_salary(sales_data, employee_data)


if __name__ == '__main__':
    main()
