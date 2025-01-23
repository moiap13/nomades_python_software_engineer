import csv
# import matplotlib.pyplot as plt
# conda install matplotlib
import os
import random

CURRENT_DIR: str = os.path.dirname(os.path.realpath(__file__))

def read_sales_data() -> list[dict[str, int|str]]:
    """
    Reads the sales data from the "sales_data.csv" file.

    Arguments: None

    Returns:
    - sales_data (list): List of dictionaries representing sales data.
    """
    sales_path: str = os.path.join(CURRENT_DIR, "sales_data.csv")
    sales_data: list[dict[str, str | int]] = []
    with open(sales_path, "r") as sales_csv_file:
        reader = csv.DictReader(sales_csv_file)
        for dict_row in reader:
            dict_row["Amount"] = int(dict_row["Amount"])
            sales_data.append(dict_row)
    return sales_data



def read_employee_data() -> list[dict[str, int|str]]:
    """
    Reads the employee data from the "employee_data.csv" file.

    Arguments: None

    Returns:
    - employee_data (list): List of dictionaries representing employee data.
    """
    employee_path: str = os.path.join(CURRENT_DIR, "employee_data.csv")
    employee_data: list[dict[str, str | int]] = []
    with open(employee_path, "r") as employee_csv_file:
        reader = csv.DictReader(employee_csv_file)
        for dict_row in reader:
            dict_row["Salary"] = int(dict_row["Salary"])
            employee_data.append(dict_row)
    return employee_data


def calculate_total_sales(sales_data: list[dict[str, int|str]]) -> int:
    """
    Calculates the total sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - total_sales (float): Total sales amount.
    """
    # total: int = 0
    # for sale_data in sales_data:
    #     total += sale_data["Amount"]
    # return total
    
    # amounts: list[int] = [sale_data["Amount"] for sale_data in sales_data]
    # return sum(amounts)

    return sum([sale_data["Amount"] for sale_data in sales_data])


def calculate_average_sales(sales_data: list[dict[str, int|str]]) -> float:
    """
    Calculates the average sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - average_sales (float): Average sales amount.
    """
    return calculate_total_sales(sales_data) / len(sales_data)

def calculate_median_sales(sales_data: list[dict[str, int|str]]) -> float:
    """
    Calculates the median sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - median_sales (float): Median sales amount.
    """
    amounts: list[int] = sorted([sale_data["Amount"] for sale_data in sales_data])
    mid: int = len(amounts) // 2
    if mid == 0:
        return -1.0
    
    # return float(amounts[mid]) if len(amounts)%2==1 else (amounts[mid-1] + amounts[mid]) / 2
    if len(amounts)%2==1: return float(amounts[mid]) 
    else: return (amounts[mid-1] + amounts[mid]) / 2 


def calculate_total_salary_expenses(employee_data: list[dict[str, int|str]]) -> int:
    """
    Calculates the total salary expenses.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - total_salary_expenses (float): Total salary expenses.
    """
    return sum([emp_data["Salary"] for emp_data in employee_data])


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
    salaries: list[int] = sorted([emp_data["Salary"] for emp_data in employee_data])
    mid: int = len(salaries) // 2
    if mid == 0:
        return -1.0
    
    # return float(amounts[mid]) if len(amounts)%2==1 else (amounts[mid-1] + amounts[mid]) / 2
    if len(salaries)%2==1: return float(salaries[mid]) 
    else: return (salaries[mid-1] + salaries[mid]) / 2


def find_employee_with_highest_sales(sales_data: list[dict[str, str | int]], employee_data: list[dict[str, str | int]]) -> tuple[str, str]:
    """
    Finds the employee with the highest sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - employee_name (str): Name of the employee with the highest sales amount.
    - department_name (str): Name of the department of the employee with the highest sales amount.
    """
    # sales_per_employee: dict[str, int] = {}
    # for sale_data in sales_data:
    #     emp_id: str = sale_data["EmployeeID"]
    #     amount: int = sale_data["Amount"]

    #     if emp_id in sales_per_employee:
    #         sales_per_employee[emp_id] = sales_per_employee[emp_id] + amount 
    #     else:
    #         sales_per_employee[emp_id] = 0 + amount

    # max_emp: str = ""
    # max_sales: int = -1e100

    # for emp_id, total_sales in sales_per_employee.items():
    #     if total_sales > max_sales:
    #         max_sales = total_sales
    #         max_emp = emp_id

    # for emp_data in employee_data:
    #     if emp_data["EmployeeID"] == max_emp:
    #         return emp_data["Name"], emp_data["Department"]
    
    # raise ValueError("Maximum not found")

    sales_per_employee: dict[str, int] = {}
    for sale_data in sales_data:
        emp_id: str = sale_data["EmployeeID"]
        amount: int = sale_data["Amount"]
        sales_per_employee[emp_id] = sales_per_employee.get(emp_id, 0) + amount
    
    # max_ = max(sales_per_employee, key=lambda emp_id: sales_per_employee[emp_id])
    max_emp: dict[str, str | int] = employee_data[int(max(sales_per_employee, key=sales_per_employee.get))-1]
    return max_emp["Name"], max_emp["Department"]

def find_department_with_highest_sales(sales_data: list[dict[str, str|int]], employee_data: list[dict[str, str|int]]) -> str:
    """
    Finds the department with the highest sales.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - department_name (str): Name of the department with the highest sales.
    """
    dep_per_emp: dict[str, str] = {}
    for emp_data in employee_data:
        dep_per_emp[emp_data["EmployeeID"]] = emp_data["Department"]
    
    sales_per_dep: dict[str, int] = {}
    for sale_data in sales_data:
        dep: str = dep_per_emp[sale_data["EmployeeID"]]
        amount: int = sale_data["Amount"]
        sales_per_dep[dep] = sales_per_dep.get(dep, 0) + amount
    return max(sales_per_dep, key=sales_per_dep.get)



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
    sales_data: list[dict[str, int|str]] = read_sales_data()

    # Read employee data
    employee_data: list[dict[str, int|str]] = read_employee_data()

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
    highest_sales_department = find_department_with_highest_sales(sales_data, employee_data)
    print("Department with Highest Sales:", highest_sales_department)

    # Plot total sales by department
    # plot_sales_by_department(sales_data, employee_data)

    # Plot sales vs. salary
    # plot_sales_vs_salary(sales_data, employee_data)


if __name__ == '__main__':
    main()
