import csv
# import matplotlib.pyplot as plt
# conda install matplotlib
import os
from functools import reduce

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def read_sales_data() -> list[dict]:
    """
    Reads the sales data from the "sales_data.csv" file.

    Arguments: None

    Returns:
    - sales_data (list): List of dictionaries representing sales data.
    """
    sales_path = CURRENT_DIR + "/sales_data.csv"
    sales_data: list[dict] = []
    with open(sales_path, 'r', newline='') as file:
        reader = csv.DictReader(file)  
        for row in reader:
            row["Amount"] = float(row["Amount"])
            sales_data.append(row)
        return sales_data

def read_employee_data():
    """
    Reads the employee data from the "employee_data.csv" file.

    Arguments: None

    Returns:
    - employee_data (list): List of dictionaries representing employee data.
    """
    employee_path = CURRENT_DIR + "/employee_data.csv"
    with open(employee_path) as employee_file:
      return [{**row, "Salary": float(row["Salary"])} for row in csv.DictReader(employee_file)]


def calculate_total_sales(sales_data: list[dict]) -> float:
    """
    Calculates the total sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - total_sales (float): Total sales amount.
    """
    # sales = 0
    # sales_count = 0

    # for sales_record in sales_data:
    #     sales += sales_record["Amount"]
    #     sales_count += 1

    # return sales, sales_count

    #def reduce_callback(pv: float, cv: dict) -> float:
    #    return pv + cv["Amount"]
        
    #return reduce(reduce_callback, sales_data, 0)
    
    return reduce(lambda pv, cv: pv + cv["Amount"] , sales_data, 0)


def calculate_average_sales(sales_data):
    """
    Calculates the average sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - average_sales (float): Average sales amount.
    """
    assert len(sales_data) > 0
    return calculate_total_sales(sales_data) / len(sales_data)

def calculate_median_sales(sales_data: list[dict]):
    """
    Calculates the median sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - median_sales (float): Median sales amount.
    """
    # all_amounts = []
    # for index in range(len(sales_data)):
    #     all_amounts.append(sales_data[index]["Amount"])
    
    # for i in range(len(all_amounts)-1):
    #     for j in range (i+1, len(all_amounts)):
    #         if all_amounts[i] > all_amounts[j]:
    #             all_amounts[i], all_amounts[j] = all_amounts[j], all_amounts[i]
  
    # if len(all_amounts) % 2 == 0:
    #     return (all_amounts[int(len(all_amounts) /2)] + all_amounts[int(len(all_amounts) // 2-1)]) / 2
    # return all_amounts[len(all_amounts)//2]

    all_amounts: list[float] = sorted([sales_data[index]["Amount"] for index in range(len(sales_data))])
    mid_point: int = len(all_amounts) // 2
    return all_amounts[mid_point] if len(all_amounts) % 2 == 1 else (all_amounts[mid_point] + all_amounts[mid_point-1]) / 2


def calculate_total_salary_expenses(employee_data: list[dict]) -> float:
    """
    Calculates the total salary expenses.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - total_salary_expenses (float): Total salary expenses.
    """
    # return sum([row["Salary"] for row in employee_data])
    return reduce(lambda pv, cv: pv + cv["Salary"], employee_data, 0)


def calculate_average_salary(employee_data):
    """
    Calculates the average salary.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - average_salary (float): Average salary.
    """
    return reduce(lambda pv, cv: pv + cv["Salary"], employee_data, 0) / len(employee_data)

def calculate_median_salary(employee_data):
    """
    Calculates the median salary.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - median_salary (float): Median salary.
    """
    all_salary: list[float] = sorted([row["Salary"] for row in employee_data])
    mid_point: int = len(all_salary) // 2
    return all_salary[mid_point] if len(all_salary) % 2 == 1 else (all_salary[mid_point] + all_salary[mid_point-1]) / 2


def find_employee_with_highest_sales(sales_data: list[dict], employee_data: list[dict]) -> tuple[float, str]:
    """
    Finds the employee with the highest sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - employee_name (str): Name of the employee with the highest sales amount.
    - department_name (str): Name of the department of the employee with the highest sales amount.
    """
    employee_sales = {}

    for employee in employee_data:
        employee_key = (employee["Name"], employee["Department"])
        curr_employee_sale: list[float] = [sale["Amount"] for sale in sales_data if sale["EmployeeID"] == employee["EmployeeID"]]
        employee_sales[employee_key] = sum(curr_employee_sale) 
    
    return max(employee_sales, key=employee_sales.get)


def find_department_with_highest_sales(sales_data, employee_data):
    """
    Finds the department with the highest sales.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - department_name (str): Name of the department with the highest sales.
    """
    department_sales = {}
    for employee in employee_data:
        curr_employee_sale: list[float] = [sale["Amount"] for sale in sales_data if sale["EmployeeID"] == employee["EmployeeID"]]

        if employee["Department"] not in department_sales:
            department_sales[employee["Department"]] = 0
        
        department_sales[employee["Department"]] = sum(curr_employee_sale) 
    
    return max(department_sales, key=department_sales.get)



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

    # Read employee data
    employee_data = read_employee_data()

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
